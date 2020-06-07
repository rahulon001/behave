# Created By Rahul Ranjan on 26/08/2018.
from features.constants import helpercodes, setter_getter
constants = {}


def request_raise(http_request_type):
    response_header, response_full, response_text, latency = \
        helpercodes.raise_request(http_request_type)
    print("Latency for the API is:", latency)
    print("API response text is ", response_text)
    print("API full response is", response_full)
    setter_getter.set_response_header(response_header)
    setter_getter.set_response_full(response_full)
    setter_getter.set_response_text(response_text)
    setter_getter.set_latency(latency)


def raise_request_multipart_secure(http_request_type):
    response_header, response_full, response_text, latency = \
        helpercodes.raise_request_multipart_secure(http_request_type)
    print("Latency for the API is:", latency)
    print("API Response is ", response_full)
    print("API Response text is ",response_text)
    setter_getter.set_response_header(response_header)
    setter_getter.set_response_full(response_full)
    setter_getter.set_response_text(response_text)
    setter_getter.set_latency(latency)


def raise_request_multipart_file_only(http_request_type):
    response_header, response_full, response_text, latency = \
        helpercodes.raise_request_multipart_file_data(http_request_type)
    print("Latency for the API is:", latency)
    print("API Response is", response_full)
    print("API Response text is ",response_text)
    setter_getter.set_response_header(response_header)
    setter_getter.set_response_full(response_full)
    setter_getter.set_response_text(response_text)
    setter_getter.set_latency(latency)


def raise_request_with_parameters(http_request_type):
    response_header, response_full, response_text, latency = \
        helpercodes.raise_request_with_parameters(http_request_type)
    print("Latency for the API is:", latency)
    print("API Response is ", response_full)
    print("API Response text is ",response_text)
    setter_getter.set_response_header(response_header)
    setter_getter.set_response_full(response_full)
    setter_getter.set_response_text(response_text)
    setter_getter.set_latency(latency)


