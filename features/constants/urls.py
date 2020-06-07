# Created By Rahul Ranjan on 26/08/2018.

baseURL_3 = "https://10.144.62.107:3001"

baseURL_5 = "http://10.144.108.127:9000"

baseURL_ = "http://10.144.108.127:9001"

baseURL_1 = "http://localhost:9000"                              # 9000

baseURL_2 = "http://10.144.8.134:3000"

baseURL_11 = "http://10.144.8.108:443"                             # 9001

baseURL_app_ = "https://api-sit.jio.com"

baseURL_app_2 = "https://api-preprod.rpay.co.in"


urlDict = \
    {
        'cmsLogin':
            baseURL_+"/legacy/login",
        'couponRetailPromoCreation':
            baseURL_+"/v1/cms/coupons/promo/",
        'convertPromoToCoupon':
            baseURL_+"/v1/cms/coupons/promo/convert",
        'couponCodeRedeeming':
            baseURL_+"/coupons/v1/coupons/redemptions",
        'couponCodeMapping':
            baseURL_+"/coupons/v1/coupons/coupon-codes",
        'GetAllCouponIDFromPromoID':
            baseURL_+"/v1/cms/coupons/promo",
        'couponCampaignCreation':
            baseURL_+"/v1/cms/coupon-campaign/",
        'CouponCodeCount':
            baseURL_+"/v1/cms/merchant/23330/coupons/",
        'couponCodeDistributionAPI':
            baseURL_+"/v1/coupons/",
        'merchant_verify':
            baseURL_+"/coupons/v1/coupons/merchant-verify",
        'checkout_coupon_code':
            baseURL_+"/coupons/v1/coupons/merchant/checkout",
        'cart_redeem':
            baseURL_+"/coupons/v1/coupons/mastercode/coupon-codes",
        'merchant_redeem':
            baseURL_+"/coupons/v1/coupons/merchant-redeem",
        'creatCouponsPullType':
            baseURL_+"/v1/cms/merchant/23331/coupon",
        'send_push_brand_coupons':
            baseURL_+"/v1/cms/merchant/",
        'send_push_merchant_coupons':
            baseURL_+"/v1/cms/merchant/",
        'add_merchant':
            baseURL_+"/v1/cms/admin/merchants",
        'add_merchant_branch_regular':
            baseURL_+"/v1/cms/merchant/",
        'add_merchant_branch':
            baseURL_+"/v1/cms/merchant/address/csv",
        "add_coupon_pull_merchant_type":
            baseURL_+"/v1/cms/merchant/",
        "add_coupon_pull_brand_type":
            baseURL_+"/v1/cms/merchant/",
        "create_merchant_group":
            baseURL_+"/v1/cms/merchant-group/",
        "create_segment":
            baseURL_+"/v1/cms/custom-user-segment/",
        "delete_user_segment":
            baseURL_+"/v1/cms/user-segment/",
        "create_coupon_group":
            baseURL_+"/v1/cms/coupon-group/",
        "create_brand":
            baseURL_+"/v1/cms/brands/",
        "get_merchant_list":
            baseURL_+"/v1/cms/admin/merchants?status=approve&page-size=0",
        "get_merchant_detail":
            baseURL_+"/v1/cms/admin/merchants/2088",
        "get_pending_merchant_list":
            baseURL_+"/v1/cms/admin/merchants?status=suspend&page-size=0",
        "get_approved_coupon_list":
            baseURL_+"/v1/cms/admin/coupons/?status=approve&valid=true",
        "get_coupon_detail":
            baseURL_+"/v1/cms/admin/coupons/70",
        "get_pending_coupon_list":
            baseURL_+"/v1/cms/admin/coupons/?status=suspend&page-size=0&page=0",
        "get_expired_coupon_list":
            baseURL_+"/v1/cms/admin/coupons/?status=approve&page-size=0&page=0&valid=expired",
        "get_reliance_retail_pending_list":
            baseURL_+"/v1/cms/coupons/promo?endTs=2018-09-04&startTs=2018-08-05&status=pending",
        "get_reliance_retail_approved_list":
            baseURL_+"/v1/cms/coupons/promo?endTs=2018-09-04&startTs=2018-08-05&status=approve",
        "get_categories":
            baseURL_+"/coupons/v1/coupons/categories?version=v5&client=myjio",
        # ====== #
        "create_reliance_retail_merchant":
            baseURL_+"/v1/cms/admin/merchants",
        "bulk_upload_reliance_retail_stores":
            baseURL_+"/v1/cms/coupons/uploadStores",
        # ======= #
        'redeemApiClientSide':
            baseURL_app_+"/cr/v2/coupons/redeem/",
        'getCouponMyjio':
            baseURL_app_+"/cr/v2/coupons?categoryId=202&start=0&end=1000&version=v4",
        'MyjioAccessToken':
            baseURL_app_+"/jm/auth/oauth/v2/token",
        'MyjioCategory':
            baseURL_app_+"/cr/v2/coupons/category?client=myjio&version=v5",
        'MyjioFavourite':
            baseURL_app_+"/cr/v2/coupons/favorites?version=v5",
        'MyjioAllCoupons':
            baseURL_app_+"/cr/v2/coupons?"
                         "categoryId=1&reductionType=2&lat=12.9716658&"
                         "lng=77.6056825&source=all&version=v5&format=group&start=0&end=10",
        "get_all_categories":
            baseURL_app_+'/v1/coupons/categories '

    }
