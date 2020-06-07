#Created By Rahul Ranjan on 24/06/2018.
@test_all1
Feature: API testing for Reliance Retail module of coupon

#  @test_coupon
  Scenario Outline: Creating and updating a Reliance Retail promotion.
    Given I am verifying "<api_name>" api with url "<url>"
    When Set URL for "<url_endpoint>" for "<http_request_type>" request
    When Set body for "<body>"
    When set header for "<header>"
    When set parameters for "None"
    When Raise "<http_request_type>" request
    Then Valid HTTP response should be received
    Then Response http code should be "<response_code>"
    Then Response HEADER content type should be "<response_header_Type>"
    Then Response BODY should not be null or empty

    Examples:
      |url_endpoint             |http_request_type|body                       |header           |api_name              |url                                                      |response_code|response_header_Type   |
      |couponRetailPromoCreation|POST             |CreatePromoRelianceRetail  |applicationJson  |Promo_creation        |http://10.144.108.127:9000/v1/cms/coupons/promo/         |200          |application/json       |
      |couponRetailPromoCreation|PUT              |CreatePromoRelianceRetail  |applicationJson  |Promo_update          |http://10.144.108.127:9000/v1/cms/coupons/promo/         |200          |application/json       |
      |couponRetailPromoCreation|GET              |None                       |None             |Get_promo_creation    |http://10.144.108.127:9000/v1/cms/coupons/promo/         |404          |application/json       |

  @test_coupon
  Scenario: Converting a promo to coupon.
    Given I am verifying "promo_to_coupon" api with url "http://10.144.108.127:9000/v1/cms/coupons/promo/"
    When Set URL for "convertPromoToCoupon" for "POST" request
    When Set data "data_convertPromoToCoupon" and file "file_convertPromoToCoupon" for api
    When set header for "multipartFormDataWithAntiForgery"
    When Raise "POST" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response HEADER content type should be "application/json"

  @test_coupon
  Scenario: Getting Coupon ID of a converted promo ID.
    Given I am verifying " get Coupon ID from Promo ID" api with url "http://10.144.108.127:9000/v1/cms/coupons/promo"
    When Set URL for "GetAllCouponIDFromPromoID" for "GET" request
    When set parameters for "GetAllCouponIDFromPromoID"
    When set header for "secureJson"
    When Raise "GET" request for secure api
    Then Response http code should be "200"
    Then Promo ID should be assigned to coupon ID.

  @test_coupon
  Scenario: Mapping the coupon codes to coupon ID.
    Given I am verifying "Mapping_coupon_code_to_couponID" api with url "http://10.144.108.127:9000/coupons/v1/coupons/coupon-codes"
    When Set URL for "couponCodeMapping" for "POST" request
    When set header for "multipartFormData"
    When Set data "None" and file "mapCouponCodeToPromo" for api
    And Raise "POST" HTTP request with file.
    Then Response http code should be "202"

  @test_coupon
  Scenario: Create a campaign for the created coupon .
    Given I am verifying "campaign creation" api with url "http://10.144.108.127:9000/v1/cms/coupon-campaign/"
    When Set URL for "couponCampaignCreation" for "POST" request
    When set header for "secureJson"
    When Set data "couponCampaignCreation" and file "None" for api
    When Raise "POST" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response BODY should not be null or empty


  @test_coupon
  Scenario: coupon code should be assigned to the coupons ID
    Given I am verifying "coupon code count" api with url "http://10.144.108.127:9000/v1/cms/merchant/23330/coupons/"
    When Set URL for "CouponCodeCount" for "GET" request
    When set header for "multipartFormDataWithAntiForgery"
    When Raise "GET" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response BODY should not be null or empty

  @test_coupon
  Scenario Outline: Assigning coupons to phone numbers .
    Given I am verifying "Assigning Coupons to phone number" api with url "http://10.144.108.127:9000/v1/coupons/5988/redeem?version=v5"
    When Set URL for "couponCodeDistributionAPI" for "POST" request
    When Set header for "couponCodeDistributionAPI" linking to user "<num>" with phone number "<phone_num>".
    When Set parameters for "couponCodeDistributionAPI"
    When Set body for "couponCodeDistributionAPI"
    When Raise "POST" request with parameters
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response HEADER content type should be "application/json"
    Then Response BODY should not be null or empty

    Examples:
      | num   |phone_num |
      |   1   |9945240312|


  @test_coupon
  Scenario: redemption of the coupon codes after coupon codes are assigned.
    Given I am verifying "Coupon code redemption" api with url "http://10.144.108.127:9000/coupons/v1/coupons/redemptions"
    When Set URL for "couponCodeRedeeming" for "POST" request
    When set header for "multipartFormData"
    When Set data "None" and file "redeemCoupon" for api
    And Raise "POST" HTTP request with file.
    Then Response http code should be "202"


  Scenario Outline: deleting a Reliance Retail promotion.
    Given I am verifying "<api_name>" api with url "<url>"
    When Set URL for "<url_endpoint>" for "<http_request_type>" request
    When Set body for "<body>"
    When set header for "<header>"
    When set parameters for "None"
    When Raise "<http_request_type>" request
    Then Valid HTTP response should be received
    Then Response http code should be "<response_code>"
    Then Response HEADER content type should be "<response_header_Type>"
    Then Response BODY should not be null or empty

    Examples:
      |url_endpoint             |http_request_type|body                       |header           |api_name              |url                                                      |response_code|response_header_Type   |
      |couponRetailPromoCreation|DELETE           |None                       |None             |Coupon_delete         |http://10.144.108.127:9000/v1/cms/coupons/promo/{promoID}|200          |application/json       |

  @test_coupon
  Scenario Outline: Create promo after removing mandatory fields one by one.
    Given I am verifying "Promo Creation" api with url "http://10.144.108.127:9000/v1/cms/coupons/promo/"
    When Set URL for "couponRetailPromoCreation" for "POST" request
    When set header for "applicationJson"
    When Set body for "CreatePromoRelianceRetail"
    And remove mandatory parameter "<parameters>" from promo body.
    When Raise "POST" request
    Then Valid HTTP response should be received
    Then Response http code should be "400"

    Examples:
      | parameters        |
      |REF_ID             |
      |PROMO_NAME         |
      |FORMAT             |
      |PROMO_STATUS       |
      |PROMO_CREATION_DATE|
      |START_DATE         |
      |END_DATE           |
      |PROMO_TYPE         |
      |TRIG_TYPE          |
      |TRIG_VAL           |
      |ARTICLE_STATUS     |
      |REWARD_TYPE        |
      |PROMO_DESC         |
      |TRANSACTION_LIMIT  |
      |COUPON_TYPE        |
      |COUPON_SERIES_NO   |

#  @test_coupon
  Scenario Outline: verifying the get APIs of merchants
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
      |url                             |api_name                          |api                              |request_type |header                          |response|response_header  |parameters               |file  |data|
      |<baseurl>/v1/cms/coupons/promo  |get_reliance_retail_pending_list  |get_reliance_retail_pending_list |GET          |multipartFormDataWithAntiForgery|200     |application/json |get_merchant_list        |None  |None|
      |<baseurl>/v1/cms/coupons/promo  |get_reliance_retail_approved_list |get_reliance_retail_approved_list|GET          |multipartFormDataWithAntiForgery|200     |application/json |None                     |None  |None|




