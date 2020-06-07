# Created By Rahul Ranjan on 26/08/2018.

from features.constants.urls import urlDict
from features.constants import setter_getter
import json, random

constants = {}


def modify_and_set_url(url_endpoint, *args):
    req = setter_getter.get_http_request_type()
    if url_endpoint == "couponRetailPromoCreation":
        if req == 'DELETE':
            constants['api_post'] = (urlDict.get(url_endpoint)+str(setter_getter.get_random_num_generator()))
        else:
            constants['api_post'] = (urlDict.get(url_endpoint))
    elif url_endpoint == "CouponCodeCount":
        constants['api_post'] = (urlDict.get(url_endpoint))+str(setter_getter.get_coupon_list()[0])+"/codes/count"
    elif url_endpoint == "redeemApiClientSide":
        constants['api_post'] = (urlDict.get(url_endpoint))+str(setter_getter.get_coupon_list()[0])
    elif url_endpoint == 'couponCodeDistributionAPI':
        constants['api_post'] = (urlDict.get(url_endpoint))+str(args[0])+'/redeem'
    elif url_endpoint == 'verify_merchant':
        constants['api_post'] = (urlDict.get(url_endpoint))
    elif url_endpoint == 'add_coupon_pull_brand_type':
        constants['api_post'] = (urlDict.get(url_endpoint))+str(setter_getter.get_merchant_grp_id())+'/coupon'
    elif url_endpoint == "send_push_brand_coupons":
        constants['api_post'] = (urlDict.get(url_endpoint))+str(setter_getter.get_merchant_grp_id())+'/coupon/' +\
                                str(setter_getter.get_cpn_id())+'/push_to_phones/csv',
    elif url_endpoint == 'add_coupon_pull_merchant_type':
        constants['api_post'] = (urlDict.get(url_endpoint))+str(random.choice(setter_getter.get_merchant_list()))+'/coupon'
    elif url_endpoint == 'add_merchant_branch_regular':
        constants['api_post'] = (urlDict.get(url_endpoint))+str(setter_getter.get_merchant_id())+'/address'
    elif url_endpoint == "send_push_merchant_coupons":
        constants['api_post'] = (urlDict.get(url_endpoint))+str(random.choice(setter_getter.get_merchant_list()))+'/coupon/' +\
                                str(setter_getter.get_cpn_id())+'/push_to_phones/csv',
    elif url_endpoint == 'delete_user_segment':
        constants['api_post'] = (urlDict.get(url_endpoint))+str(json.loads(setter_getter.get_response_text())['id'])
    elif url_endpoint == 'create_coupon_group':
        if req == 'DELETE':
            constants['api_post'] = (urlDict.get(url_endpoint))+str(json.loads(setter_getter.get_response_text())['id'])
        else:
            constants['api_post'] = (urlDict.get(url_endpoint))
    elif url_endpoint == 'create_brand':
        if req == 'DELETE':
            constants['api_post'] = (urlDict.get(url_endpoint))+str(json.loads(setter_getter.get_response_text())['id'])
        else:
            constants['api_post'] = (urlDict.get(url_endpoint))
    else:
        constants['api_post'] = (urlDict.get(url_endpoint))
    setter_getter.set_url(constants['api_post'])
