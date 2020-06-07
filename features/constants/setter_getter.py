import os, random, string
constants = {}

path = os.path.dirname(__file__)


def get_path():
    return path
# =======


def set_brand_external_id_list(external_id):
    constants['brand_list'] = external_id


def get_brand_external_id_list():
    return constants['brand_list']


def set_brand_id(brand_id):
    constants['brand_id'] = brand_id


def get_brand_id():
    return constants['brand_id']


def set_brand_id_lst(brand_id_lst):
    constants['brand_id_lst'] = brand_id_lst


def get_brand_id_lst():
    return constants['brand_id_lst']


def set_category_id(category_id):
    constants['category_id'] = category_id


def get_category_id():
    return constants['category_id']


def set_merchant_list(merchant_list):
    constants['merchant_list'] = merchant_list


def get_merchant_list():
    return constants['merchant_list']


def set_merchant_id(merchant_id):
    constants['merchant_id'] = merchant_id


def get_merchant_id():
    return constants['merchant_id']


def set_response_header(response_header):
    constants['response_header'] = response_header


def get_response_header():
    return constants['response_header']


def set_response_full(response_full):
    constants['response_full'] = response_full


def get_response_full():
    return constants['response_full']


def set_response_text(response_text):
    constants['response_text'] = response_text


def get_response_text():
    return constants['response_text']


def set_latency(latency):
    constants['latency'] = latency


def get_latency():
    return constants['latency']


def set_http_request_type(http_request_type):
    constants["http_request_type"] = http_request_type


def get_http_request_type():
    return constants["http_request_type"]


def set_random_char_generator(rang):
    constants['random_char'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(rang))


def get_random_char_generator():
    return constants['random_char']


def set_promo_list(promo_list):
    constants["promo_list"] = promo_list


def get_promo_list():
    return constants["promo_list"]


def set_coupon_list(coupon_list):
    constants["coupon_list"] = coupon_list


def get_coupon_list():
    return constants["coupon_list"]


def set_random_num_generator(lower_lmt, upper_lmt):
    constants['random'] = random.randint(lower_lmt, upper_lmt)


def get_random_num_generator():
    return constants['random']


def set_merchant_grp_id(resp_txt):
    constants['resp_txt'] = resp_txt


def get_merchant_grp_id():
    return constants['resp_txt']


def set_url(api_post):
    # print(api_post)
    constants['api_post'] = api_post


def get_url():
    return constants['api_post']


def set_redeem_code(coupon_code):
    constants['coupon_code'] = coupon_code


def get_redeem_code():
    return constants['coupon_code']


def set_header(api_request_header):
    constants['api_request_Header'] = api_request_header


def get_header():
    return constants['api_request_Header']


def set_parameter(set_parameters):
    constants['setParameters'] = set_parameters


def get_parameter():
    return constants['setParameters']


def set_body(api_body):
    constants['api_Body'] = api_body


def get_body():
    return constants['api_Body']


def set_file(file):
    constants['api_file_multipart'] = file


def get_file():
    return constants['api_file_multipart']


def set_data(data):
    constants['api_data_multipart'] = data


def get_data():
    return constants['api_data_multipart']


def set_anti_forge(x_anti_forgery):
    constants['x_anti_forgery'] = x_anti_forgery


def get_anti_forge():
    return constants['x_anti_forgery']


def set_response(response_full):
    constants['response_full'] = response_full


def get_response():
    return constants['response_full']


def set_user_numbers(users):
    constants['users'] = users


def get_user_numbers():
    return constants['users']


def set_external_id(ext_id):
    constants['external_id'] = ext_id


def get_external_id():
    return constants['external_id']


def set_sku_details(sku_details):
    constants['sku_details'] = sku_details


def get_sku_details():
    return constants['sku_details']


def set_cpn_id(coupon_id):
    constants['cpn_id'] = coupon_id


def get_cpn_id():
    return constants['cpn_id']


def set_mas_id_list(mas_id_list):
    # print(mas_id_list)
    constants['mas_id_lst'] = mas_id_list


def get_mas_id_list():
    return constants['mas_id_lst']


def set_mas_id(mas_id):
    constants['mas_id'] = mas_id


def get_mas_id():
    return constants['mas_id']


def set_sku_id(random_sku):
    constants['sku'] = random_sku


def get_sku_id():
    return constants['sku']


def set_sku_list(sku_list):
    constants['sku_list'] = sku_list


def get_sku_list():
    return constants['sku_list']


def set_coupon_id_lst(coupon_id_list):
    constants['coupon_id_list'] = coupon_id_list


def get_coupon_id_lst():
    return constants['coupon_id_list']


def set_coupon_code_lst(coupon_code_lst):
    constants['coupon_code_lst'] = coupon_code_lst


def get_coupon_code_lst():
    return constants['coupon_code_lst']


def set_sku_id_list_rr(sku_id_list_rr):
    constants['sku_id_list_rr'] = sku_id_list_rr


def get_sku_id_list_rr():
    return constants['sku_id_list_rr']


def set_merchant_grp_id_lst(merchants_group_id_list):
    constants['merchants_group_id_list'] = merchants_group_id_list


def get_merchant_grp_id_lst():
    return constants['merchants_group_id_list']


def set_mas_id_updated_list(mas_id_list):
    constants['mas_id_list'] = mas_id_list


def get_mas_id_updated_list():
    return constants['mas_id_list']


def set_merchant_branch_data(raw_data):
    constants['branch_data'] = raw_data


def get_merchant_branch_data():
    return constants['branch_data']


def set_segment_list(segment_list):
    constants['segment_list'] = segment_list


def get_segment_list():
    return constants['segment_list']


def set_segment_CMS_id(segment_id_list):
    constants['segment_id_list'] = segment_id_list


def get_segment_CMS_id():
    return constants['segment_id_list']


def set_value(any_value):
    constants['any_value'] = any_value


def get_value():
    return constants['any_value']


def set_coupon_list_chunk(i):
    constants['i'] = i


def get_coupon_list_chunk():
    return constants['i']