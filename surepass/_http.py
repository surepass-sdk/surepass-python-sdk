import abc
import logging
import requests
from .exceptions import SurepassAPIException, AuthorizationTokenExpiredException


class SurepassHTTPClient(abc.ABC):
    API_BASE_URL = "https://kyc-api.aadhaarkyc.io/api/v1"

    def __init__(self, client):
        self.client = client
        self.session = requests.Session()

    @property
    def headers(self):
        return {
            "Authorization": "Bearer {}".format(self.client.config.authorization_token)
        }

    def request(self, method, route, **kwargs):
        url = self.API_BASE_URL + route
        headers = kwargs.pop("headers", None) or {}
        headers.update(self.headers)
        try:
            response = self.session.request(method, url, headers=headers, **kwargs)
        except Exception as exc:
            logging.exception(exc)
            raise SurepassAPIException from exc

        if response.status_code == 401:
            raise AuthorizationTokenExpiredException

        return response
