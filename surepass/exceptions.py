class SurepassAPIException(Exception):
    pass


class AuthorizationTokenExpiredException(SurepassAPIException):
    pass


class InvalidOtpException(SurepassAPIException):
    pass
