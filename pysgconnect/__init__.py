# -*- coding: UTF-8 -*-

URLS = {
    'PRD': 'https://sso.sgmarkets.com',
}

def get_url(env):
    return URLS[env]

from .SGConnectAuth import SGConnectAuth
