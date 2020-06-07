from features.constants import helpercodes
from features.constants import setter_getter
from features.constants.api_parameters import set_url
from features.constants.api_parameters import set_body
from features.constants.api_parameters import set_headers
from features.constants.api_parameters import set_request
from features.constants.api_parameters import set_parameters
import os, json


from datetime import datetime
now = datetime.now()
path = os.path.dirname(__file__)


def set_merchant_list():
    merchant_list = []
    merchant_list.append(setter_getter.get_response_text())
    setter_getter.set_merchant_list(merchant_list)


def create_merchant_group_id():
    # helpercodes.login_to_cms()
    set_body.modify_and_set_data_files('create_merchant_group', None, setter_getter.get_merchant_list())
    set_url.modify_and_set_url('create_merchant_group')
    set_headers.modify_and_set_headers('secureJson')
    set_request.raise_request_multipart_secure('POST')
    helpercodes.verify_response('200')
    t = (setter_getter.get_response_text())
    setter_getter.set_merchant_grp_id(json.loads(t)["id"])


def set_url_merchant_group(url_endpoint, http_request_type):
    set_body.modify_and_set_data_files('create_merchant_group', None, setter_getter.get_merchant_list())


def set_external_brand_id():
    setter_getter.set_random_char_generator(5)
    setter_getter.set_brand_external_id_list(setter_getter.get_random_char_generator())
    setter_getter.set_external_id(setter_getter.get_random_char_generator())


def create_brand():
    brand_id_lst = []
    setter_getter.set_http_request_type('POST')
    set_url.modify_and_set_url('create_brand')
    set_external_brand_id()
    set_body.modify_and_set_data_files('data_create_brand', 'file_create_brand')
    set_headers.modify_and_set_headers('multipartFormDataWithAntiForgery')
    set_request.raise_request_multipart_secure('POST')
    brand_id = (json.loads(setter_getter.get_response_text()))['id']
    brand_id_lst.append(brand_id)
    setter_getter.set_brand_id_lst(brand_id_lst)


def get_coupon_categories():
    category_list = []
    setter_getter.set_http_request_type('GET')
    set_url.modify_and_set_url('get_categories')
    set_headers.modify_and_set_headers('get_request_myjio')
    set_parameters.modify_and_set_parameters('Category')
    set_request.raise_request_with_parameters('GET')
    for i in range(len(json.loads(setter_getter.get_response_text())["categories"])):
        category_list.append(json.loads(setter_getter.get_response_text())["categories"][i]["id"])
    setter_getter.set_category_id('|'.join(map(str,category_list)))


def push_brand_coupon_to_number():
    setter_getter.set_http_request_type('POST')
    set_url.modify_and_set_url('send_push_brand_coupons')
    set_headers.modify_and_set_headers('get_request_myjio')
    set_request.raise_request_with_parameters('POST')


def push_merchant_coupon_to_number():
    setter_getter.set_http_request_type('POST')
    set_url.modify_and_set_url('send_push_merchant_coupons')
    set_headers.modify_and_set_headers('get_request_myjio')
    set_request.raise_request_with_parameters('POST')


def set_coupon_id():
    coupon_id = (json.loads(setter_getter.get_response_text()))['id']
    setter_getter.set_cpn_id(coupon_id)
