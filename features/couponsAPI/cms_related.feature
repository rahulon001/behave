@test_all
Feature: verifying the get APIs
  @test_coupon1
  Scenario Outline: verifying the get APIs
    Given I am verifying "<api_name>" api with url "<url>"
    When Set URL for "<api>" for "<request_type>" request
    When Set data "<data>" and file "<file>" for api
    When set header for "<header>"
    When set parameters for "<parameters>"
    When Raise "<request_type>" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "<response>"
    Then Response HEADER content type should be "<response_header>"
    Examples:
      |url                                               |api_name                 |api                       |request_type |header                          |response|response_header  |parameters               |file |data|
      |<baseurl>/v1/cms/admin/merchants                  |get_merchant_list        |get_merchant_list         |GET          |multipartFormDataWithAntiForgery|200     |application/json |get_merchant_list        |None  |None|
      |<baseurl>/v1/cms/admin/merchants/2088             |get_merchant_detail      |get_merchant_detail       |GET          |multipartFormDataWithAntiForgery|200     |application/json |None                     |None  |None|
      |<baseurl>/v1/cms/admin/merchants                  |get_pending_merchant_list|get_pending_merchant_list |GET          |multipartFormDataWithAntiForgery|200     |application/json |get_pending_merchant_list|None  |None|
      |<baseurl>/v1/cms/admin/coupons/                   |get_approved_coupon_list |get_approved_coupon_list  |GET          |multipartFormDataWithAntiForgery|200     |application/json |get_approved_coupon_list |None  |None|
      |<baseurl>/v1/cms/admin/coupons/8395               |get_coupon_detail        |get_coupon_detail         |GET          |multipartFormDataWithAntiForgery|200     |application/json |None                     |None  |None|
      |<baseurl>/v1/cms/admin/coupons                    |get_pending_coupon_list  |get_pending_coupon_list   |GET          |multipartFormDataWithAntiForgery|200     |application/json |get_pending_coupon_list  |None  |None|
      |<baseurl>/v1/cms/admin/coupons                    |get_expired_coupon_list  |get_expired_coupon_list   |GET          |multipartFormDataWithAntiForgery|200     |application/json |get_expired_coupon_list  |None  |None|
      |<baseurl>/v1/cms/brands/                          |get_brand_list           |create_brand              |GET          |multipartFormDataWithAntiForgery|200     |application/json |None                     |None  |None|
