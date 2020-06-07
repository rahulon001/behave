from behave import *
from features.sourcecode import creation


@when(u'Set URL for "{url_endpoint}" for "{http_request_type}" request for merchant group')
def step_impl(context, url_endpoint, http_request_type):
    creation.set_url_merchant_group(url_endpoint, http_request_type)


@then(u'create the merchant group id with the merchant list.')
def step_impl(context):
    creation.create_merchant_group_id()


@when(u'create a brand')
def step_impl(context):
    creation.create_brand()


@when(u'set an external brand ID')
def step_impl(context):
    creation.set_external_brand_id()


@when(u'set merchant id')
def step_impl(context):
    creation.set_merchant_list()


@when(u'get coupon categories')
def step_impl(context):
    creation.get_coupon_categories()


@when(u'I push the push brand type coupon to the designated number')
def step_impl(context):
    creation.push_brand_coupon_to_number()


@when(u'I push the push merchant type coupon to the designated number')
def step_impl(context):
    creation.push_merchant_coupon_to_number()


@then(u'set coupon id')
def steo_impl(context):
    creation.set_coupon_id()