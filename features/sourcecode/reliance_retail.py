# Created By Rahul Ranjan on 24/06/2018.
from features.constants.api_parameters import set_url
from features.constants.api_parameters import set_body
from features.constants.api_parameters import set_headers
from features.constants.api_parameters import set_parameters
from features.constants.api_parameters import set_request
from features.constants import helpercodes, setter_getter
import json
from datetime import datetime


now = datetime.now()


# json data
def set_url_(url_endpoint, http_request_type):
    setter_getter.set_http_request_type(http_request_type)
    set_url.modify_and_set_url(url_endpoint)


# api_body
def modify_set_simple_body(data):
    set_body.modify_and_set_simple_body(data)


# Secure_api_body
def set_body_data_file(data, file):
    set_body.modify_and_set_data_files(data, file)


# header
def set_header(header, phone_num=None):
    set_headers.modify_and_set_headers(header)
    setter_getter.set_user_numbers(phone_num)


# parameters
def set_parameter(params):
    set_parameters.modify_and_set_parameters(params)

# ================================================================================ #


def request_raise(http_request_type):
    set_request.request_raise(http_request_type)


def raise_request_multipart_secure(http_request_type):
    set_request.raise_request_multipart_secure(http_request_type)


def raise_request_multipart_file_only(http_request_type):
    set_request.raise_request_multipart_file_only(http_request_type)

# ================================================================================ #


def promo_id_to_coupon_id():
    coupon_lst = []
    json_data = json.loads(setter_getter.get_response_text())
    for x in setter_getter.get_promo_list():
        for elements in json_data:
            # print(elements['REF_ID'])
            if elements['REF_ID'] == str(x):
                c = elements["COUPON"]
            else:
                continue
            coupon_lst.append(c)
        # constants['coupon_lst'] = couponLst
        setter_getter.set_coupon_list([6026, 6953])

def change_mandatory_params(parameters):
    set_body.change_mandatory_parameters(parameters)


def validate_response():
    helpercodes.validate_responcee()


def expected_response(expected_response_code):
    helpercodes.verify_response(expected_response_code)


def expected_header_content_type(expected_response_content_type):
    response_header = setter_getter.get_response_header()
    actual_response_content_type = response_header['Content-Type']
    # print(actual_response_content_type)
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + \
                      actual_response_content_type


def check_response_body():
    s = setter_getter.get_response_full()
    if None in s:
        assert False, '***ERROR:  Null or none response body received'


# def coupon_code_redemption(redeem_coupon):
#     constants['api_file_multipart'] = apiBodyDict.get(redeem_coupon)

    # print("F"*100,http_request_body['api_file_multipart'])


def login_to_cms():
    helpercodes.login_to_cms()


# if __name__ == "__main__":
#     modifysetBODY('CreatePromoRelianceRetail')
