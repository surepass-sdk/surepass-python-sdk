from ._config import SurepassAPIConfig
from .aadhaar import AadhaarHTTPClient
from .RC import RCHTTPClient


class SurepassClient(object):

    def __init__(self, authorization_token):
        self.config = SurepassAPIConfig(authorization_token=authorization_token)
        self.aadhaar = AadhaarHTTPClient(self)
        self.rc_number = RCHTTPClient(self)
