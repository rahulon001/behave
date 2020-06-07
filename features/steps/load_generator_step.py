from behave import *
from features.sourcecode import load_generator


@when(u'set given brands in a list')
def step_impl(context):
    load_generator.set_brand_list()


@when(u'get list of existing brand id')
def step_impl(context):
    load_generator.set_existing_brand_list()


@when(u'get list of existing merchant groups')
def step_impl(context):
    load_generator.set_existing_merchant_group_list()


@when(u'get list of existing coupon IDs')
def step_impl(context):
    load_generator.set_existing_coupon_list()


@when(u'create {brand_num:d} brands with the given brand ids and store it in a list')
def step_impl(context, brand_num):
    load_generator.create_brands(brand_num)


@when(u'refreshing the address_info.csv file')
def step_impl(context):
    load_generator.deleting_address_info()

@when(u'create {merchants_num:d} merchants in "{city}" with coordinate {lat} and {long} each with {branches_num} branches within {radius_branch} km radius')
def step_impl(context, city, lat, long,merchants_num, branches_num, radius_branch):
    load_generator.create_multiple_merchants(city, lat, long, merchants_num, branches_num, radius_branch)


# @when(u'create {merchants_num:d} merchants each with {branches_num:d} branches within {radius_branch:d} km radius')
# def step_impl(context,merchants_num, branches_num, radius_branch):
#     load_generator.create_multiple_merchants(merchants_num, branches_num, radius_branch)


@when(u'create {coupon_num:d} coupons from all types')
def step_impl(context, coupon_num):
    load_generator.create_multiple_coupons(coupon_num)


@then(u'create the merchant group with the merchant list.')
def step_impl(context):
    load_generator.create_merchant_group()


@then(u'creating campaigns with all the created coupon IDs')
def step_impl(context):
    load_generator.create_campaigns()


@when(u'verify and redeem {coupon_code:d} coupon code for merchant')
def step_impl(context, coupon_code):
    load_generator.assign_verify_user_to_coupon(coupon_code)


@when(u'Create {num:d} promo to be converted.')
def step_impl(context, num):
    load_generator.create_promo(num)


@when(u'set masId for merchants')
def step_impl(context):
    load_generator.set_mas_id()


@when(u'set random data list')
def step_impl(context):
    load_generator.set_random_data_list()


@when(u'create {num:d} coupons with {merchants_num:d} "{city}" {lat}  {long} {branches_num} {radius_branch} as parameters')
def step_impl(context, num, city, lat, long,merchants_num, branches_num, radius_branch):
    load_generator.create_multiple_coupons_along_with_all_entities(city, lat, long, merchants_num, branches_num, radius_branch, num)


@when(u'create {segment_number:d} external segments')
def step_impl(context, segment_number):
    load_generator.create_segments(segment_number)


@when(u'create {num:d} users and link them to segment ids')
def step_impl(context, num):
    load_generator.link_user_to_segments(num)
