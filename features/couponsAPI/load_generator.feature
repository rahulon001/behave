
 @test_all11
Feature: Creating load for performance tests

  Scenario: creating brand load for PE for test data generation
    Given I am verifying "brand creation" api with url "<base_url>/v1/cms/brands/"
#    When set given brands in a list
#    When set random data list
#    When create 40 brands with the given brand ids and store it in a list

  @create_coupon
  Scenario: getting existing brand for PE for test data generation
    Given I am verifying "get brand ID" api with url "<base_url>/v1/cms/brands/"
    When get list of existing brand id

  @create_coupon
  Scenario: getting existing merchant groups for test data generation
    Given I am verifying "get merchant group" api with url "<base_url>/v1/cms/merchant-group/"
    When get list of existing merchant groups

  @targeting_data
  Scenario: getting existing coupons for test data generation
    Given I am verifying "get coupon" api with url "<base_url>/v1/cms/merchant-group/"
    When get list of existing coupon IDs


#  @target_load
  Scenario Outline: creating merchant load for PE for test data generaion
    Given I am verifying "brand creation" api with url "<base_url>/v1/cms/brands/"
    Given I am verifying "merchant_creation" api with url "<base_url>/v1/cms/admin/merchants"
    Given I am verifying "merchant_branch_creation" api with url "<base_url>v1/cms/merchant/address/csv"
    Given I am verifying "merchant_group_creation" api with url "<base_url>/v1/cms/merchant-group/"
    Given I am verifying "Coupon_creation" api with url "<base_url>/v1/cms/merchant/2344/coupon"
    Given I am verifying "Campaign_creation" api with url "<base_url>/v1/cms/coupon-campaign/"

    When refreshing the address_info.csv file
    # keep merchant quantity 250 or more
    When set masId for merchants
    When create <merchant_quantity> merchants in "<city>" with coordinate <latitude> and <longitude> each with <branch_quantity> branches within <radius> km radius
#    Then create the merchant group with the merchant list.
  Examples:Test2
  |merchant_quantity|city      |latitude |longitude|branch_quantity|radius|
  |2               |Bangalore |12.972442|77.580643|1              |25    |
  |2               |Mumbai    |19.125362|72.999199|1              |25    |
  |2                |Chennai   |13.067439|80.237617|1              |25    |
  |2               |Hyderabad |17.38714 |78.491684|1              |25    |
  |2                |Ahmedabad |23.033863|72.585022|1              |25    |
  |2                |Kolkata   |22.572645|88.363892|1              |24    |

#  Examples:
#  |merchant_quantity|city      |latitude |longitude|branch_quantity|radius|
#  |319              |Bangalore |12.972442|77.580643|1              |25    |
#  |1753             |Mumbai    |19.125362|72.999199|1              |25    |
#  |2240             |Chennai   |13.067439|80.237617|1              |25    |
#  |2846             |Hyderabad |17.38714 |78.491684|1              |25    |
#  |2005             |Ahmedabad |23.033863|72.585022|1              |25    |
#  |2303             |Kolkata   |22.572645|88.363892|1              |24    |




#  @target_load
  Scenario: creating coupon load for PE data generation
    When get coupon categories
  # keep coupon quantity 250 or more
    When create 50 coupons from all types
    Then creating campaigns with all the created coupon IDs



  Scenario:verify redeem coupon code for merchant
    Given I am verifying "redeem_coupon_client_side" api with url "<base_url>/v1/coupons/13558/redeem"
    Given I am verifying "coupon combination for SKU Cart" api with url "<base_url>/coupons/v1/mastercode/coupon-codes"
    Given I am verifying "Merchant verify" api with url "<base_url>coupons/v1/coupons/merchant-verify"
    Given I am verifying "Merchant Checkout" api with url "<base_url>coupons/v1/coupons/merchant/checkout"
    Given I am verifying "Merchant redeem" api with url "<base_url>/coupons/v1/coupons/merchant-redeem"

    When verify and redeem 1 coupon code for merchant


  @target_load
  Scenario: Create External_segments
    # always keep segments in multiple of 10 and any number users
      When create 10 external segments
      When create 3 users and link them to segment ids


#  @target_load
  Scenario Outline: creating user load for PE for targeting
    Given I am verifying "redeem_coupon_client_side" api with url "<base_url>/v1/coupons/13558/redeem"
    Given I am verifying "redeem_coupon_client_side" api with url "<base_url>/v1/coupons/13558/redeem"

    When get coupon categories
    # always keep multiple of 5 coupons
    When create 10 coupons with <merchant_quantity> "<city>" <latitude>  <longitude> <branch_quantity> <radius> as parameters
  Examples: Test1
    |merchant_quantity|city      |latitude |longitude|branch_quantity|radius|
    |1                |Bangalore |12.972442|77.580643|1              |25    |
#    |1                |Mumbai    |19.125362|72.999199|1              |25    |
#    |1                |Chennai   |13.067439|80.237617|1              |25    |
#    |1                |Hyderabad |17.38714 |78.491684|1              |25    |
#    |1                |Ahmedabad |23.033863|72.585022|1              |25    |
#    |1                |Kolkata   |22.572645|88.363892|1              |24    |

   Scenario:Create segments and campaigns for coupons for targeting
     When create 10 segments