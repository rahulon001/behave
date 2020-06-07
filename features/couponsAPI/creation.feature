@test_all
Feature: Test for creating different entities like merchants , coupons etc.
#  @test_coupon
  Scenario: Creating a merchant
    Given I am verifying "add_Merchant" api with url "<baseurl>/v1/cms/admin/merchants"
    When Set URL for "add_merchant" for "POST" request
    When Set data "data_add_merchants" and file "file_add_merchants" for api
#    When I am logging in to CMS
    When set header for "multipartFormDataWithAntiForgery"
    When Raise "POST" request for secure api
    When set merchant id
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response HEADER content type should be "application/json"


  Scenario: Creating a merchant group id
    Then create the merchant group id with the merchant list.


  Scenario: Create a brand ID
    When create a brand

  Scenario: get coupon categories and set them
    When get coupon categories


  Scenario Outline: Creating a merchant pull type coupon
    Given I am verifying "<api_name>" api with url "<url>"
    When Set URL for "<api>" for "<request_type>" request
    When Set data "<data>" and file "<file>" for api
    When set header for "<header>"
    When Raise "<request_type>" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "<response>"
    Then Response HEADER content type should be "<response_header>"

    Examples:
      |url                                           |api_name                                                 |api                          |request_type|file                                                          |data                                                           |header                          |response|response_header  |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_flat_discount_on_sku       |add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_flat_discount_on_sku       |data_add_coupon_pull_merchant_type_flat_discount_on_sku        |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_Free_SKUs_on_Bill          |add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_Free_SKUs_on_Bill          |data_add_coupon_pull_merchant_type_Free_SKUs_on_Bill           |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_Free_SKUs_on_SKUs          |add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_Free_SKUs_on_SKUs          |data_add_coupon_pull_merchant_type_Free_SKUs_on_SKUs           |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_flat_discount              |add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_flat_discount              |data_add_coupon_pull_merchant_type_flat_discount               |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_Percentage_discount_on_SKU |add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_Percentage_discount_on_SKU |data_add_coupon_pull_merchant_type_Percentage_discount_on_SKU  |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_Percentage_discount_on_Bill|add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_Percentage_discount_on_Bill|data_add_coupon_pull_merchant_type_Percentage_discount_on_Bill |multipartFormDataWithAntiForgery|200     |application/json |

#   @test_coupon
  Scenario Outline: Creating a brand pull type coupon
    Given I am verifying "<api_name>" api with url "<url>"
    When Set URL for "<api>" for "<request_type>" request
    When Set data "<data>" and file "<file>" for api
    When set header for "<header>"
    When Raise "<request_type>" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "<response>"
    Then Response HEADER content type should be "<response_header>"
    Examples:
      |url                                               |api_name                                              |api                       |request_type|file                                                       |data                                                       |header                          |response|response_header  |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_flat_discount_on_sku       |add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_flat_discount_on_sku       |data_add_coupon_pull_brand_type_flat_discount_on_sku       |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_Free_SKUs_on_SKUs          |add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_Free_SKUs_on_SKUs          |data_add_coupon_pull_brand_type_Free_SKUs_on_SKUs          |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_Free_SKUs_on_Bill          |add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_Free_SKUs_on_Bill          |data_add_coupon_pull_brand_type_Free_SKUs_on_Bill          |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_flat_discount              |add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_flat_discount              |data_add_coupon_pull_brand_type_flat_discount              |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_Percentage_discount_on_SKU |add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_Percentage_discount_on_SKU |data_add_coupon_pull_brand_type_Percentage_discount_on_SKU |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_Percentage_discount_on_Bill|add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_Percentage_discount_on_Bill|data_add_coupon_pull_brand_type_Percentage_discount_on_Bill|multipartFormDataWithAntiForgery|200     |application/json |


  Scenario Outline: Creating and pushing a brand push type coupon to a number
    Given I am verifying "<api_name>" api with url "<url>"
    When Set URL for "<api>" for "<request_type>" request
    When Set data "<data>" and file "<file>" for api
    When set header for "<header>"
    When Raise "<request_type>" request for secure api
    Then set coupon id
    Then Valid HTTP response should be received
    Then Response http code should be "<response>"
    Then Response HEADER content type should be "<response_header>"
    When I push the push brand type coupon to the designated number
    Then Valid HTTP response should be received
    #
    Examples:
      |url                                               |api_name                                              |api                       |request_type|file                                                       |data                                                       |header                          |response|response_header  |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_push_brand_type_Free_SKUs_on_Bill          |add_coupon_pull_brand_type|POST        |file_add_coupon_push_brand_type_Free_SKUs_on_Bill          |data_add_coupon_push_brand_type_Free_SKUs_on_Bill          |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_push_brand_type_flat_discount_on_sku       |add_coupon_pull_brand_type|POST        |file_add_coupon_push_brand_type_flat_discount_on_sku       |data_add_coupon_push_brand_type_flat_discount_on_sku       |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_push_brand_type_Free_SKUs_on_SKUs          |add_coupon_pull_brand_type|POST        |file_add_coupon_push_brand_type_Free_SKUs_on_SKUs          |data_add_coupon_push_brand_type_Free_SKUs_on_SKUs          |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_push_brand_type_flat_discount              |add_coupon_pull_brand_type|POST        |file_add_coupon_push_brand_type_flat_discount              |data_add_coupon_push_brand_type_flat_discount              |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_push_brand_type_Percentage_discount_on_SKU |add_coupon_pull_brand_type|POST        |file_add_coupon_push_brand_type_Percentage_discount_on_SKU |data_add_coupon_push_brand_type_Percentage_discount_on_SKU |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_push_brand_type_Percentage_discount_on_Bill|add_coupon_pull_brand_type|POST        |file_add_coupon_push_brand_type_Percentage_discount_on_Bill|data_add_coupon_push_brand_type_Percentage_discount_on_Bill|multipartFormDataWithAntiForgery|200     |application/json |


  Scenario Outline: Creating and pushing a merchant push type coupon to a number
    Given I am verifying "<api_name>" api with url "<url>"
    When Set URL for "<api>" for "<request_type>" request
    When Set data "<data>" and file "<file>" for api
    When I am logging in to CMS
    When set header for "<header>"
    When Raise "<request_type>" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "<response>"
    Then Response HEADER content type should be "<response_header>"
    When I push the push merchant type coupon to the designated number
    Then Valid HTTP response should be received

#
    Examples:
      |url                                           |api_name                                                 |api                          |request_type|file                                                          |data                                                           |header                          |response|response_header  |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_push_merchant_type_Free_SKUs_on_Bill          |add_coupon_pull_brand_type   |POST        |file_add_coupon_push_merchant_type_Free_SKUs_on_Bill          |data_add_coupon_push_merchant_type_Free_SKUs_on_Bill           |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_push_merchant_type_flat_discount_on_sku       |add_coupon_pull_merchant_type|POST        |file_add_coupon_push_merchant_type_flat_discount_on_sku       |data_add_coupon_push_merchant_type_flat_discount_on_sku        |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_push_merchant_type_Free_SKUs_on_SKUs          |add_coupon_pull_merchant_type|POST        |file_add_coupon_push_merchant_type_Free_SKUs_on_SKUs          |data_add_coupon_push_merchant_type_Free_SKUs_on_SKUs           |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_push_merchant_type_flat_discount              |add_coupon_pull_merchant_type|POST        |file_add_coupon_push_merchant_type_flat_discount              |data_add_coupon_push_merchant_type_flat_discount               |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_push_merchant_type_Percentage_discount_on_SKU |add_coupon_pull_merchant_type|POST        |file_add_coupon_push_merchant_type_Percentage_discount_on_SKU |data_add_coupon_push_merchant_type_Percentage_discount_on_SKU  |multipartFormDataWithAntiForgery|200     |application/json |
      |<baseurl>/v1/cms/merchant/<merchant_id>/coupon|add_coupon_push_merchant_type_Percentage_discount_on_Bill|add_coupon_pull_merchant_type|POST        |file_add_coupon_push_merchant_type_Percentage_discount_on_Bill|data_add_coupon_push_merchant_type_Percentage_discount_on_Bill |multipartFormDataWithAntiForgery|200     |application/json |





#  @test_coupon
  Scenario: creating coupon group
    Given I am verifying "coupon group creation" api with url "<base_url>/v1/cms/coupon-group/"
    When Set URL for "create_coupon_group" for "POST" request
    When set header for "multipartFormDataWithAntiForgery"
    When Set data "data_create_coupon_group" and file "file_create_coupon_group" for api
    When Raise "POST" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response BODY should not be null or empty

#  @test_coupon
  Scenario: deleting coupon group
    Given I am verifying "segment deletion" api with url "<base_url>/v1/cms/coupon-group/<id>"
    When Set URL for "create_coupon_group" for "DELETE" request
    When set header for "multipartFormDataWithAntiForgery"
    When Raise "DELETE" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response BODY should not be null or empty

#  @test_coupon
  Scenario: creating the segment for coupons
    Given I am verifying "segment creation" api with url "<base_url>/v1/cms/custom-user-segment/"
    When Set URL for "create_segment" for "POST" request
    When set header for "secureJson"
    When Set data "create_segment" and file "None" for api
    When Raise "POST" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response BODY should not be null or empty


#  @test_coupon
  Scenario: deleting the segment for coupons
    Given I am verifying "segment deletion" api with url "<base_url>/v1/cms/custom-user-segment/<id>"
    When Set URL for "delete_user_segment" for "DELETE" request
    When set header for "multipartFormDataWithAntiForgery"
    When Raise "DELETE" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response BODY should not be null or empty

#  @test_coupon
  Scenario: creating brand
    Given I am verifying "brand creation" api with url "<base_url>/v1/cms/brands/"
    When Set URL for "create_brand" for "POST" request
    When set an external brand ID
    When set header for "multipartFormDataWithAntiForgery"
    When Set data "data_create_brand" and file "file_create_brand" for api
    When Raise "POST" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response BODY should not be null or empty

#  @test_coupon
  Scenario: deleting brand
    Given I am verifying "segment deletion" api with url "<base_url>/v1/cms/brands/<id>"
    When Set URL for "create_brand" for "DELETE" request
    When set header for "multipartFormDataWithAntiForgery"
    When Raise "DELETE" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response BODY should not be null or empty