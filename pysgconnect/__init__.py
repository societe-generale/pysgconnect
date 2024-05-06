# -*- coding: UTF-8 -*-

URLS = {
    "PRD": "https://sso.sgmarkets.com",
}


def get_url(env):
    return URLS[env]


from .sg_connect_auth import SGConnectAuth
from .token import Token
