# Created By Rahul Ranjan on 26/08/2018.

from features.constants import helpercodes,setter_getter
from features.constants.apiBody import headerType
import random

constants = {}


def modify_and_set_headers(header=None):
    if header in ("multipartFormDataWithAntiForgery", "secureJson"):
        constants['api_request_Header'] = helpercodes.edit_header(headerType.get(header))
    elif header in "couponCodeDistributionAPI":
        constants['phone_num'] = str(setter_getter.get_user_numbers())
        constants['api_request_Header'] = (headerType.get(header))
        constants['api_request_Header']['x-loginid'] = constants['phone_num']
    elif header in "merchant_redeem":
        constants['api_request_Header'] = (headerType.get(header))
        constants['api_request_Header']['x-loginid'] = constants['phone_num']
    elif header in ('Category', 'Favourite', 'AllCoupons'):
        constants['api_request_Header'] = (headerType.get(header))
        constants['api_request_Header']['Authorization'] = 'Bearer '+helpercodes.access_token()
    else:
        constants['api_request_Header'] = (headerType.get(header))
    setter_getter.set_header(constants['api_request_Header'])
