import logging
from datetime import datetime, timedelta, timezone

from requests import Response, Session
from requests.auth import AuthBase

from . import get_url
from .token import Token


class SGConnectAuth(AuthBase):
    """
    Authentication class to use with requests to protect calls by SGConnect OAuth2 protocol
    """

    def __init__(self, client_id, client_secret, env="PRD", scopes=None):
        if isinstance(scopes, str):
            scopes = [scopes]

        self._logger: logging.Logger = logging.getLogger(__name__)
        self._endpoint: str = f"{get_url(env)}/sgconnect/oauth2/access_token"
        self._session: Session = Session()
        self._token: Token = Token()

        self._credentials = (client_id, client_secret)
        self._scopes: list[str] | None = scopes

    def __call__(self, r):
        self._check_token()
        r.headers["Authorization"] = f"Bearer {self._token.jwt}"
        return r

    def _check_token(self) -> None:
        if self._token.is_not_empty() and not self._token.is_token_expired():
            self._logger.debug("Current token valid until: %s", self._token.expires_at)
            return

        if not self._scopes:
            raise ValueError("No scopes were provided")

        response: Response = self._session.post(
            self._endpoint,
            verify=True,
            auth=self._credentials,
            data={"grant_type": "client_credentials", "scopes": " ".join(self._scopes)},
        )

        response.raise_for_status()

        body = response.json()

        token_value = body["access_token"]
        expire_value = body["expires_in"]

        if not token_value or not expire_value:
            raise ValueError("access_token or expires_in field are not present")

        self._token = Token(
            jwt=token_value,
            expires_at=datetime.now(timezone.utc) + timedelta(seconds=expire_value),
        )
        self._logger.debug("New access token valid until: %s", expire_value)
