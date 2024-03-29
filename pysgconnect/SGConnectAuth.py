# -*- coding: UTF-8 -*-

from requests.auth import AuthBase
import requests
from datetime import datetime, timedelta
from . import get_url
import logging

logger = logging.getLogger(__name__)

class SGConnectAuth(AuthBase):
    """
    Authentication class to use with requests to protect calls by SGConnect OAuth2 protocol
    """

    def __init__(self, client_id, client_secret, env='PRD', scopes=None):
        if isinstance(scopes, str):
            scopes = [scopes]

        self._env = env
        self._client_id = client_id
        self._client_secret = client_secret
        self._scopes = scopes

        self._token = None
        self._token_cre_time = None
        self._token_exp_time = None

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer %s' % self._getAccessToken()
        return r

    def _getTokenEndpoint(self):
        return '%s/sgconnect/oauth2/access_token' % get_url(self._env)

    def _getAccessToken(self):
        if self._token is None or self._token_exp_time <= datetime.utcnow():
            logger.info('Get a new access token from SGConnect with "%s" scopes and "%s" client id.',
                        ','.join(self._scopes),
                        self._client_id)

            requests.packages.urllib3.disable_warnings()
            r = requests.post(self._getTokenEndpoint(),
                              verify=True,
                              auth=(self._client_id, self._client_secret),
                              data={
                                  'grant_type': 'client_credentials',
                                  'scope': ' '.join(self._scopes)
                              })

            content = r.json()
            now = datetime.utcnow()

            r.raise_for_status()
            assert content['access_token'], 'No access token in response'

            self._token_cre_time = now
            self._token_exp_time = now + timedelta(seconds=content['expires_in'])
            self._token = content['access_token']

            logger.debug('New access token valid until: %s', self._token_exp_time.isoformat())

        return self._token
