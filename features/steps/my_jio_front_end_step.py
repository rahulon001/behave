from behave import *
from features.sourcecode import my_jio_front_end

@when(u'I am logging in for access token')
def step_impl(context):
    my_jio_front_end.set_access_token()

@when(u'Raise "{http_request_type}" request with parameters')
def step_impl(context, http_request_type):
    my_jio_front_end.raise_request_with_parameters(http_request_type)

