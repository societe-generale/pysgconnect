"""
Testing token behaviour
"""

import time

import pytest
import requests

from pysgconnect.sg_connect_auth import SGConnectAuth


def test_uninitialized_token(requests_mock):
    adapter = requests_mock.post(
        "https://sso.sgmarkets.com/sgconnect/oauth2/access_token",
        json={"access_token": "hzefjzezelfjeaofe", "expires_in": 120},
        status_code=200,
    )

    auth = SGConnectAuth("client_id", "client_secret", scopes=["admin"])

    requests_mock.get(
        "https://jsonplaceholder.typicode.com/", text="resp", status_code=200
    )
    resp = requests.get("https://jsonplaceholder.typicode.com/", auth=auth)
    resp = requests.get("https://jsonplaceholder.typicode.com/", auth=auth)

    assert (
        resp.request.headers["Authorization"] == "Bearer hzefjzezelfjeaofe"
    ), "Token is wrong"
    assert adapter.call_count == 1, "Auth server called more than once"


def test_unauthorized_token(requests_mock):
    adapter = requests_mock.post(
        "https://sso.sgmarkets.com/sgconnect/oauth2/access_token",
        json={"access_token": "hzefjzezelfjeaofe", "expires_in": 120},
        status_code=403,
    )

    requests_mock.get(
        "https://jsonplaceholder.typicode.com/", text="resp", status_code=200
    )

    with pytest.raises(requests.HTTPError):
        requests.get(
            "https://jsonplaceholder.typicode.com/",
            auth=SGConnectAuth("client_id", "client_secret", scopes=["admin"]),
        )

    assert adapter.call_count == 1, "Auth server called more than once"


def test_token_refresh(requests_mock):
    adapter = requests_mock.post(
        "https://sso.sgmarkets.com/sgconnect/oauth2/access_token",
        json={"access_token": "hzefjzezelfjeaofe", "expires_in": 2},
        status_code=200,
    )

    session = requests.Session()
    session.auth = SGConnectAuth("client_id", "client_secret", scopes=["admin"])

    requests_mock.get(
        "https://jsonplaceholder.typicode.com/", text="resp", status_code=200
    )
    resp = session.get("https://jsonplaceholder.typicode.com/")

    assert (
        resp.request.headers["Authorization"] == "Bearer hzefjzezelfjeaofe"
    ), "Token is wrong"

    time.sleep(5)

    resp = session.get("https://jsonplaceholder.typicode.com/")

    assert adapter.call_count == 2, "Auth did not asked for a new token"
