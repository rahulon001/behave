from features.constants import helpercodes
from features.constants.api_parameters import set_request


def raise_request_with_parameters(http_request_type):
        set_request.raise_request_with_parameters(http_request_type)


def set_access_token():
    helpercodes.access_token()
