from shutil import rmtree

import pandas as pd
from requests import Session
import requests
import random, os, datetime, json, string
from datetime import datetime
from time import time
from dateutil.relativedelta import *

now = datetime.now()
s = Session()
constants = {}
merchants_group_id_list = []

path1 = os.path.dirname(__file__) + "/features/constants"

baseURL = "http://10.144.108.127:3301"

mgid = ['821', '823']
# mgid = ['3025']

brand = [64621, 64622, 64623, 64624, 64625, 64626, 64627, 64628, 64629, 64630, 64631, 64632, 64633, 64634, 64635, 64636,
         64637, 64638, 64639, 64640, 64641, 64642, 64643, 64644, 64645, 64646, 64647, 64648, 64649, 64650, 64651, 64652,
         64653, 64654, 64655, 64656, 64657, 64658, 64659, 64660, 64661, 64662, 64663, 64664, 64665, 64666, 64667, 64668,
         64669, 64670, 64671, 64672, 64673, 64674, 64675, 64676, 64677, 64678, 64679, 64680, 64681, 64682, 64683, 64684,
         64685, 64686, 64687, 64688, 64689, 64690, 64691, 64692, 64693, 64694, 64695, 64696, 64697, 64698, 64699, 64700,
         64701, 64702, 64703, 64704, 64705, 64706, 64707, 64708, 64709, 64710, 64711, 64712, 64713, 64714, 64715, 64716,
         64717, 64718, 64719, 64720]


# brand = [100922, 3]


def skuid(): return str(random.randint(18000, 24000))


def skuid1(): return str(random.randint(28001, 32000))


def skuid2(): return str(random.randint(35001, 38000))


def random_number(): return int(round(time() * 1000))


payment_type_coupon = {
    'file_add_coupon_pull_brand_type_flat_discount': {
        'file': ('B.jpg', open(path1 + '/images/B.jpg', 'rb'), 'image/jpeg')
    },
    'data_add_coupon_pull_brand_type_flat_discount': {
        "redeemDays": "1|2|3|4|5|6|7",
        "redeemMinTime": "0",
        "redeemMaxTime": "24",
        "redeemMinAge": "0",
        "redeemMaxAge": "150",
        "redeemableOnline": "1",
        "discountCoupon": "0",
        "isUniversalCode": "0",
        "redeemGender": "MALE",
        "locations": "all",
        "couponType": "2",
        "clients[]": ["2", "1"],
        "skuConditionType": "1",
        "skuOfferType": "1",
        "discountType": "FLAT_DISCOUNT",
        "discountExtraRules": "12",
        "discountAbsValue": "10",
        "discountMinBill": "100",
        "couponStartTime": "2018-08-23T12:41:07.598677",
        "couponEndTime": "2018-08-23T12:41:07.598677",
        "categories": "2|3|12|11",
        "title": "10_rs_off_on_all_products",
        "pushType": "0",
        "isLimitedRedeem": "true",
        "couponTag": "1",
        "source": "prime",
        "merchantGroup": "721",
        "brand": "621",
        "startDate": "2018/08/06",
        "endDate": "2018/08/31",
        "couponUrl": "https://www.google.com",
        "affiliateUrl": "https://www.google.com",
        "description": "Test Coupons Online and physical both",
        "terms": "Test Coupons Online and physical both",
        "couponLabel": "TESTCoupon",
        "couponCode": "$GENERATE_PER_CUSTOMER",
        "redeemCap": "2",
        "maxRedeem": "200",
        "priv": "0",
        "validFrom": "2018/08/06 00:00:00",
        "validTo": "2018/08/31 23:59:00",
        "redeemHours": "0|24",
        "redeemLocation": "1",
        "reductionType": "1",
        "url": "https://www.google.com",
        "redeem-age-interval": "0|150",
        "status": "APPROVE",
        "subscribe": "true",
        "userGroup": "42"

    },
    'file_add_coupon_pull_brand_type_Free_SKUs_on_Bill': {
        'file': ('A.jpg', open(path1 + '/images/A.jpg', 'rb'), 'image/jpeg')
    },
    'data_add_coupon_pull_brand_type_Free_SKUs_on_Bill': {
        "redeemDays": "1|2|3|4|5|6|7",
        "redeemMinTime": "0",
        "redeemMaxTime": "24",
        "redeemMinAge": "0",
        "redeemMaxAge": "150",
        "discountCoupon": "0",
        "redeemableOnline": "1",
        "isUniversalCode": "0",
        "redeemGender": "MALE",
        "locations": "all",
        "couponType": "2",
        "clients[]": ["2", "1"],
        "discountType": "FREE_SKU_WITH_BILL",
        "discountExtraRules": "12",
        "discountAbsValue": "10",
        "skuOffer": "10036387 |10036553",
        "skuOfferName": "Rs.30 off on buying 2 Tide Naturals 800g",
        "skuOfferQuantity": "1",
        "discountMinBill": "100",
        "skuConditionSellingPrice": "110",
        "couponStartTime": "2018-08-23T12:41:07.598677",
        "couponEndTime": "2018-08-23T12:41:07.598677",
        "categories": "2|3|12|11",
        "title": "rin_on_100_rs_purchase",
        "pushType": "0",
        "isLimitedRedeem": "true",
        "couponTag": "1",
        "source": "prime",
        "merchantGroup": "721",
        "brand": "621",
        "startDate": "2018/08/06",
        "endDate": "2018/08/31",
        "couponUrl": "https://www.google.com",
        "affiliateUrl": "https://www.google.com",
        "description": "Test Coupons Online and physical both",
        "terms": "Test Coupons Online and physical both",
        "couponLabel": "TESTCoupon",
        "couponCode": "$GENERATE_PER_CUSTOMER",
        "redeemCap": "2",
        "maxRedeem": "200",
        "priv": "0",
        "validFrom": "2018/08/06 00:00:00",
        "validTo": "2018/08/31 23:59:00",
        "redeemHours": "0|24",
        "redeemLocation": "1",
        "reductionType": "1",
        "url": "https://www.google.com",
        "redeem-age-interval": "0|150",
        "status": "APPROVE",
        "subscribe": "true",
        "userGroup": "42"

    },
    'file_add_coupon_pull_brand_type_Free_SKUs_on_SKUs': {
        'file': ('C.jpg', open(path1 + '/images/C.jpg', 'rb'), 'image/jpeg')
    },
    'data_add_coupon_pull_brand_type_Free_SKUs_on_SKUs': {
        "title": "1 rin on 1kg ariel",
        "couponLabel": "TESTCoupon",
        "couponType": "2",
        "clients[]": [
            "3",
            "7",
            "2"
        ],
        "source": "prime",
        "pushType": "0",
        "couponTag": "3",
        "discountType": "FREE_SKU_WITH_SKU",
        "discountExtraRules": "12",
        "startDate": "2019-11-29",
        "couponStartTime": "2019-11-28T18:30:00.000Z",
        "endDate": "2022-05-31",
        "couponEndTime": "2022-05-31T18:29:00.000Z",
        "imageURL": "/cr/v2/coupons/images/l,00000001.jpeg",
        "fullImageUrl": "",
        "redeemGender": "MALE",
        "redeemMinAge": "0",
        "redeemMaxAge": "150",
        "redeemableOnline": "1",
        "couponUrl": "https://google.com",
        "affiliateUrl": "https://google.com",
        "description": "Test Coupons Online and physical both",
        "terms": "Test Coupons Online and physical both",
        "createTs": "1578492211000",
        "status": "APPROVE",
        "redeemCap": "10000000",
        "maxRedeem": "10000000",
        "merchantRedeemCap": "10000000",
        "couponCode": "$GENERATE_PER_CUSTOMER",
        "isLimitedRedeem": "true",
        "locations": "all",
        "demoCoupon": "0",
        "discountCoupon": "1",
        "discountCouponRadio": "true",
        "perCartRedeem": "1",
        "merchantGroup": "581",
        "brand": "99374",
        "skuConditionType": "1",
        "skuCondition": "78678876876",
        "skuConditionName": "Pantene Total Damage Control 80ml",
        "skuConditionQuantity": "2",
        "skuConditionActualPrice": "100",
        "skuConditionSellingPrice": "110",
        "isUniversalCode": "0",
        "redeemDays": "1|2|3|4|5|6|7",
        "redeemMinTime": "0",
        "redeemMaxTime": "24",
        "categories": "30210|30002|70100|70101|20002|20202",
        "skuOfferType": "1",
        "skuOffer": "10021580299353",
        "skuOfferName": "RIN",
        "skuOfferQuantity": "1",
        "priv": "0",
        "validFrom": "2019/11/29 00:00:00",
        "validTo": "2022/05/31 23:59:00",
        "redeemHours": "0|24",
        "redeemLocation": "1",
        "reductionType": "1",
        "url": "https://google.com",
        "redeem-age-interval": "0|150",
        "subscribe": "true",
        "userGroup": "42"
    },
    'file_add_coupon_pull_brand_type_flat_discount_on_sku': {
        'file': ('D.jpg', open(path1 + '/images/D.jpg', 'rb'), 'image/jpeg')
    },
    'data_add_coupon_pull_brand_type_flat_discount_on_sku': {
        "title": "coupon1578492546944",
        "couponLabel": "TESTCoupon",
        "couponType": "2",
        "clients[]": [
            "2",
            "3",
            "7"
        ],
        "source": "discover",
        "pushType": "0",
        "couponTag": "3",
        "discountType": "FLAT_DISCOUNT_WITH_SKU",
        "discountExtraRules": "12",
        "startDate": "2020-01-08",
        "couponStartTime": "2020-01-08T14:09:00.000Z",
        "endDate": "2021-01-07",
        "couponEndTime": "2021-01-07T14:09:00.000Z",
        "imageURL": "/cr/v2/coupons/images/m6PZY1-GYuHgU29tkAoZfg",
        "redeemGender": "OTHER",
        "redeemMinAge": "0",
        "redeemMaxAge": "150",
        "redeemableOnline": "1",
        "couponUrl": "https://www.google.com",
        "affiliateUrl": "https://www.google.com",
        "description": "Test Coupons Online and physical both",
        "terms": "Test Coupons Online and physical both",
        "createTs": "1578498617000",
        "status": "APPROVE",
        "redeemCap": "1000000",
        "maxRedeem": "1000000",
        "merchantRedeemCap": "10000000",
        "couponCode": "$GENERATE_PER_CUSTOMER",
        "isLimitedRedeem": "true",
        "locations": "all",
        "demoCoupon": "0",
        "discountCoupon": "1",
        "discountCouponRadio": "true",
        "perCartRedeem": "1",
        "merchantGroup": "3025",
        "brand": "100922",
        "skuConditionType": "1",
        "skuCondition": "10099666",
        "skuConditionName": "RIN",
        "skuConditionQuantity": "1",
        "skuConditionActualPrice": "121",
        "skuConditionSellingPrice": "115",
        "discountAbsValue": "6",
        "isUniversalCode": "0",
        "redeemDays": "1|2|3|4|5|6|7",
        "redeemMinTime": "0",
        "redeemMaxTime": "24",
        "categories": "20202|30210|30002|70100|70101",
        "priv": "0",
        "validFrom": "2020/01/08 19:39:00",
        "validTo": "2021/01/07 19:39:00",
        "redeemHours": "0|24",
        "redeemLocation": "1",
        "reductionType": "1",
        "url": "https://www.google.com",
        "redeem-age-interval": "0|150",
        "subscribe": "true",
        "userGroup": "42"

    },
    'file_add_coupon_pull_brand_type_Percentage_discount_on_SKU': {
        'file': ('E.jpg', open(path1 + '/images/E.jpg', 'rb'), 'image/jpeg')
    },
    'data_add_coupon_pull_brand_type_Percentage_discount_on_SKU': {
        "title": "coupon1578492546944",
        "couponLabel": "TESTCoupon",
        "couponType": "2",
        "clients[]": [
            "7",
            "2",
            "3"
        ],
        "source": "discover",
        "pushType": "0",
        "couponTag": "3",
        "discountType": "PERCENTAGE_DISCOUNT_WITH_SKU",
        "discountExtraRules": "12",
        "startDate": "2020-01-08",
        "couponStartTime": "2020-01-08T14:09:06.000Z",
        "endDate": "2021-01-07",
        "couponEndTime": "2021-01-07T14:09:06.000Z",
        "redeemGender": "OTHER",
        "redeemMinAge": "0",
        "redeemMaxAge": "150",
        "redeemableOnline": "1",
        "couponUrl": "https://www.google.com",
        "affiliateUrl": "https://www.google.com",
        "description": "Test Coupons Online and physical both",
        "terms": "Test Coupons Online and physical both",
        "createTs": "1578493042000",
        "status": "APPROVE",
        "redeemCap": "1000000",
        "maxRedeem": "1000000",
        "merchantRedeemCap": "10000000",
        "couponCode": "$GENERATE_PER_CUSTOMER",
        "isLimitedRedeem": "true",
        "locations": "all",
        "demoCoupon": "0",
        "discountCoupon": "1",
        "discountCouponRadio": "true",
        "perCartRedeem": "1",
        "merchantGroup": "3025",
        "brand": "100922",
        "isUniversalCode": "0",
        "redeemDays": "1|2|3|4|5|6|7",
        "redeemMinTime": "0",
        "redeemMaxTime": "24",
        "categories": "2|3|20202|30210|30002",
        "categoriesByClient": "[object Object]",
        "discountPercentageValue": "15",
        "discountMax": "15",
        "skuCondition": "10099666871",
        "skuConditionName": "RIN",
        "skuConditionQuantity": "2",
        "skuConditionActualPrice": "100",
        "skuConditionSellingPrice": "115",
        "skuConditionType": "1",
        "priv": "0",
        "validFrom": "2020/01/08 19:39:00",
        "validTo": "2021/01/07 19:39:00",
        "redeemHours": "0|24",
        "redeemLocation": "1",
        "reductionType": "1",
        "url": "https://www.google.com",
        "redeem-age-interval": "0|150",
        "subscribe": "true",
        "userGroup": "42"

    },
    'file_add_coupon_pull_brand_type_Percentage_discount_on_Bill': {
        'file': ('F.jpg', open(path1 + '/images/F.jpg', 'rb'), 'image/jpeg')
    },
    'data_add_coupon_pull_brand_type_Percentage_discount_on_Bill': {
        "redeemDays": "1|2|3|4|5|6|7",
        "redeemMinTime": "0",
        "redeemMaxTime": "24",
        "redeemMinAge": "0",
        "discountCoupon": "0",
        "redeemMaxAge": "150",
        "redeemableOnline": "1",
        "isUniversalCode": "0",
        "redeemGender": "MALE",
        "locations": "all",
        "couponType": "2",
        "couponStartTime": "2018-08-23T12:41:07.598677",
        "couponEndTime": "2018-08-23T12:41:07.598677",
        "title": "10% off on a minimum bill amount of Rs. 500",
        "pushType": "0",
        "isLimitedRedeem": "true",
        "couponTag": "1",
        "source": "prime",
        "discountType": "PERCENTAGE_DISCOUNT",
        "merchantGroup": "721",
        "brand": "621",
        "clients[]": ["2", "1"],
        "categories": "2|3|12|11",
        "skuConditionType": "1",
        "skuOfferType": "1",
        "discountPercentageValue": "10",
        "discountMax": "100",
        "discountMinBill": "1000",
        "startDate": "2018/08/06",
        "endDate": "2018/08/31",
        "couponUrl": "https://www.google.com",
        "affiliateUrl": "https://www.google.com",
        "description": "Test Coupons Online and physical both",
        "terms": "Test Coupons Online and physical both",
        "couponLabel": "TESTCoupon",
        "couponCode": "$GENERATE_PER_CUSTOMER",
        "redeemCap": "2",
        "maxRedeem": "200",
        "priv": "0",
        "validFrom": "2018/08/06 00:00:00",
        "validTo": "2018/08/31 23:59:00",
        "redeemHours": "0|24",
        "redeemLocation": "1",
        "reductionType": "1",
        "url": "https://www.google.com",
        "redeem-age-interval": "0|150",
        "status": "APPROVE",
        "subscribe": "true",
        "userGroup": "42"

    },
    'file_add_coupon_push_brand_type_Free_SKUs_on_Bill': {
        'file': ('G.jpg', open(path1 + '/images/G.jpg', 'rb'), 'image/jpeg')
    },
    'data_add_coupon_push_brand_type_Free_SKUs_on_Bill': {
        "redeemDays": "1|2|3|4|5|6|7",
        "redeemMinTime": "0",
        "redeemMaxTime": "24",
        "redeemMinAge": "0",
        "redeemMaxAge": "150",
        "redeemableOnline": "1",
        "isUniversalCode": "0",
        "discountCoupon": "0",
        "redeemGender": "MALE",
        "locations": "all",
        "couponType": "2",
        "clients[]": ["2", "1"],
        "discountType": "FREE_SKU_WITH_BILL",
        "discountExtraRules": "12",
        "discountAbsValue": "10",
        "skuOffer": "10036387 |10036553",
        "skuOfferName": "Rs.30 off on buying 2 Tide Naturals 800g",
        "skuOfferQuantity": "1",
        "discountMinBill": "100",
        "skuConditionSellingPrice": "110",
        "couponStartTime": "2018-08-23T12:41:07.598677",
        "couponEndTime": "2018-08-23T12:41:07.598677",
        "categories": "2|3|12|11",
        "title": "rin_on_100_rs_purchase",
        "pushType": "1",
        "isLimitedRedeem": "true",
        "couponTag": "1",
        "source": "prime",
        "merchantGroup": "721",
        "brand": "621",
        "startDate": "2018/08/06",
        "endDate": "2018/08/31",
        "couponUrl": "https://www.google.com",
        "affiliateUrl": "https://www.google.com",
        "description": "Test Coupons Online and physical both",
        "terms": "Test Coupons Online and physical both",
        "couponLabel": "TESTCoupon",
        "couponCode": "$GENERATE_PER_CUSTOMER",
        "redeemCap": "2",
        "maxRedeem": "200",
        "priv": "1",
        "validFrom": "2018/08/06 00:00:00",
        "validTo": "2018/08/31 23:59:00",
        "redeemHours": "0|24",
        "redeemLocation": "1",
        "reductionType": "1",
        "url": "https://www.google.com",
        "redeem-age-interval": "0|150",
        "status": "APPROVE",
        "subscribe": "true"
    },
    'file_add_coupon_push_brand_type_flat_discount': {
        'file': ('H.jpg', open(path1 + '/images/H.jpg', 'rb'), 'image/jpeg')
    },
    'data_add_coupon_push_brand_type_flat_discount': {
        "redeemDays": "1|2|3|4|5|6|7",
        "redeemMinTime": "0",
        "redeemMaxTime": "24",
        "redeemMinAge": "0",
        "redeemMaxAge": "150",
        "redeemableOnline": "1",
        "isUniversalCode": "0",
        "redeemGender": "MALE",
        "locations": "all",
        "discountCoupon": "0",
        "couponType": "2",
        "clients[]": ["2", "1"],
        "skuConditionType": "1",
        "skuOfferType": "1",
        "discountType": "FLAT_DISCOUNT",
        "discountExtraRules": "12",
        "discountAbsValue": "10",
        "discountMinBill": "100",
        "couponStartTime": "2018-08-23T12:41:07.598677",
        "couponEndTime": "2018-08-23T12:41:07.598677",
        "categories": "2|3|12|11",
        "title": "10_rs_off_on_all_products",
        "pushType": "0",
        "isLimitedRedeem": "true",
        "couponTag": "1",
        "source": "prime",
        "merchantGroup": "721",
        "brand": "621",
        "startDate": "2018/08/06",
        "endDate": "2018/08/31",
        "couponUrl": "https://www.google.com",
        "affiliateUrl": "https://www.google.com",
        "description": "Test Coupons Online and physical both",
        "terms": "Test Coupons Online and physical both",
        "couponLabel": "TESTCoupon",
        "couponCode": "$GENERATE_PER_CUSTOMER",
        "redeemCap": "2",
        "maxRedeem": "200",
        "priv": "0",
        "validFrom": "2018/08/06 00:00:00",
        "validTo": "2018/08/31 23:59:00",
        "redeemHours": "0|24",
        "redeemLocation": "1",
        "reductionType": "1",
        "url": "https://www.google.com",
        "redeem-age-interval": "0|150",
        "status": "APPROVE",
        "subscribe": "true"
    },
    'file_brand_type_Free_SKUs_on_SKUs_PushType': {
        'file': ('I.jpg', open(path1 + '/images/I.jpg', 'rb'), 'image/jpeg')
    },
    'data_brand_type_Free_SKUs_on_SKUs_PushType':
        {
            "id": "11681",
            "title": "coupon1578562205742",
            "couponLabel": "TESTCoupon",
            "couponType": "2",
            "clients[]": [
                "2",
                "3",
                "7"
            ],
            "source": "prime",
            "pushType": "1",
            "couponTag": "3",
            "discountType": "FREE_SKU_WITH_SKU",
            "discountExtraRules": "12",
            "startDate": "2020-01-09",
            "couponStartTime": "2020-01-09T09:30:05.000Z",
            "endDate": "2021-01-08",
            "couponEndTime": "2021-01-08T09:30:05.000Z",
            "imageURL": "/cr/v2/coupons/images/m7KnghSQJYbgU29tkAqCvA",
            "fullImageUrl": "http://10.144.108.127:443/coupons/v1/images/m7KnghSQJYbgU29tkAqCvA",
            "redeemGender": "MALE",
            "redeemMinAge": "0",
            "redeemMaxAge": "150",
            "redeemableOnline": "1",
            "couponUrl": "https://google.com",
            "affiliateUrl": "https://google.com",
            "description": "Test Coupons Online and physical both",
            "terms": "Test Coupons Online and physical both",
            "createTs": "1578562205000",
            "status": "APPROVE",
            "redeemCap": "1000000",
            "maxRedeem": "1000000",
            "merchantRedeemCap": "10000000",
            "couponCode": "$GENERATE_PER_CUSTOMER",
            "isLimitedRedeem": "true",
            "locations": "all",
            "demoCoupon": "0",
            "discountCoupon": "0",
            "perCartRedeem": "1",
            "merchantGroup": "3025",
            "brand": "100922",
            "skuConditionType": "1",
            "skuCondition": "18652|33978",
            "skuConditionName": "Pantene Total Damage Control 80ml",
            "skuConditionQuantity": "2",
            "skuConditionActualPrice": "100",
            "skuConditionSellingPrice": "110",
            "skuOfferType": "1",
            "skuOffer": "21890|47206",
            "skuOfferName": "RIN",
            "skuOfferQuantity": "1",
            "isUniversalCode": "0",
            "redeemDays": "1|2|3|4|5|6|7",
            "redeemMinTime": "0",
            "redeemMaxTime": "24",
            "categories": "20002|20202|30210|30002|70100|70101",
            "categoriesByClient": "[object Object]",
            "file": "(binary)",
            "priv": "1",
            "validFrom": "2020/01/09 15:00:00",
            "validTo": "2021/01/08 15:00:00",
            "redeemHours": "0|24",
            "redeemLocation": "1",
            "reductionType": "1",
            "url": "https://google.com",
            "redeem-age-interval": "0|150",
            "subscribe": "true",
            "userGroup": "42"
        },
    'file_brand_type_flat_discount_on_sku_PushType': {
        'file': ('J.jpg', open(path1 + '/images/J.jpg', 'rb'), 'image/jpeg')
    },
    'data_brand_type_flat_discount_on_sku_PushType': {

        "title": "coupon1578492546944",
        "couponLabel": "TESTCoupon",
        "couponType": "2",
        "clients[]": [
            "2",
            "3",
            "7"
        ],
        "source": "discover",
        "pushType": "0",
        "couponTag": "3",
        "discountType": "FLAT_DISCOUNT_WITH_SKU",
        "discountExtraRules": "12",
        "startDate": "2020-01-08",
        "couponStartTime": "2020-01-08T14:09:00.000Z",
        "endDate": "2021-01-07",
        "couponEndTime": "2021-01-07T14:09:00.000Z",
        "imageURL": "/cr/v2/coupons/images/m6PZY1-GYuHgU29tkAoZfg",
        "redeemGender": "OTHER",
        "redeemMinAge": "0",
        "redeemMaxAge": "150",
        "redeemableOnline": "1",
        "couponUrl": "https://www.google.com",
        "affiliateUrl": "https://www.google.com",
        "description": "Test Coupons Online and physical both",
        "terms": "Test Coupons Online and physical both",
        "createTs": "1578498617000",
        "status": "APPROVE",
        "redeemCap": "1000000",
        "maxRedeem": "1000000",
        "merchantRedeemCap": "10000000",
        "couponCode": "$GENERATE_PER_CUSTOMER",
        "isLimitedRedeem": "true",
        "locations": "all",
        "demoCoupon": "0",
        "discountCoupon": "1",
        "discountCouponRadio": "true",
        "perCartRedeem": "1",
        "merchantGroup": "3025",
        "brand": "100922",
        "skuConditionType": "1",
        "skuCondition": "10099666",
        "skuConditionName": "RIN",
        "skuConditionQuantity": "1",
        "skuConditionActualPrice": "121",
        "skuConditionSellingPrice": "115",
        "discountAbsValue": "6",
        "isUniversalCode": "0",
        "redeemDays": "1|2|3|4|5|6|7",
        "redeemMinTime": "0",
        "redeemMaxTime": "24",
        "categories": "20202|30210|30002|70100|70101",
        "priv": "0",
        "validFrom": "2020/01/08 19:39:00",
        "validTo": "2021/01/07 19:39:00",
        "redeemHours": "0|24",
        "redeemLocation": "1",
        "reductionType": "1",
        "url": "https://www.google.com",
        "redeem-age-interval": "0|150",
        "subscribe": "true",
        "userGroup": "42"

    },
    'file_brand_type_Percentage_discount_on_SKU_PushType': {
        'file': ('K.jpg', open(path1 + '/images/K.jpg', 'rb'), 'image/jpeg')
    },
    'data_brand_type_Percentage_discount_on_SKU_PushType':
        {
            "title": "coupon1578492546944",
            "couponLabel": "TESTCoupon",
            "couponType": "2",
            "clients[]": [
                "7",
                "2",
                "3"
            ],
            "source": "discover",
            "pushType": "0",
            "couponTag": "3",
            "discountType": "PERCENTAGE_DISCOUNT_WITH_SKU",
            "discountExtraRules": "12",
            "startDate": "2020-01-08",
            "couponStartTime": "2020-01-08T14:09:06.000Z",
            "endDate": "2021-01-07",
            "couponEndTime": "2021-01-07T14:09:06.000Z",
            "redeemGender": "OTHER",
            "redeemMinAge": "0",
            "redeemMaxAge": "150",
            "redeemableOnline": "1",
            "couponUrl": "https://www.google.com",
            "affiliateUrl": "https://www.google.com",
            "description": "Test Coupons Online and physical both",
            "terms": "Test Coupons Online and physical both",
            "createTs": "1578493042000",
            "status": "APPROVE",
            "redeemCap": "1000000",
            "maxRedeem": "1000000",
            "merchantRedeemCap": "10000000",
            "couponCode": "$GENERATE_PER_CUSTOMER",
            "isLimitedRedeem": "true",
            "locations": "all",
            "demoCoupon": "0",
            "discountCoupon": "1",
            "discountCouponRadio": "true",
            "perCartRedeem": "1",
            "merchantGroup": "3025",
            "brand": "100922",
            "isUniversalCode": "0",
            "redeemDays": "1|2|3|4|5|6|7",
            "redeemMinTime": "0",
            "redeemMaxTime": "24",
            "categories": "2|3|20202|30210|30002",
            "categoriesByClient": "[object Object]",
            "discountPercentageValue": "15",
            "discountMax": "15",
            "skuCondition": "10099666871",
            "skuConditionName": "RIN",
            "skuConditionQuantity": "2",
            "skuConditionActualPrice": "100",
            "skuConditionSellingPrice": "115",
            "skuConditionType": "1",
            "priv": "0",
            "validFrom": "2020/01/08 19:39:00",
            "validTo": "2021/01/07 19:39:00",
            "redeemHours": "0|24",
            "redeemLocation": "1",
            "reductionType": "1",
            "url": "https://www.google.com",
            "redeem-age-interval": "0|150",
            "subscribe": "true",
            "userGroup": "42"
        },
    'file_add_coupon_push_brand_type_Percentage_discount_on_Bill': {
        'file': ('L.jpg', open(path1 + '/images/L.jpg', 'rb'), 'image/jpeg')
    },
    'data_add_coupon_push_brand_type_Percentage_discount_on_Bill': {
        "redeemDays": "1|2|3|4|5|6|7",
        "redeemMinTime": "0",
        "redeemMaxTime": "24",
        "redeemMinAge": "0",
        "redeemMaxAge": "150",
        "redeemableOnline": "1",
        "isUniversalCode": "0",
        "redeemGender": "MALE",
        "locations": "all",
        "discountCoupon": "0",
        "couponType": "2",
        "couponStartTime": "2018-08-23T12:41:07.598677",
        "couponEndTime": "2018-08-23T12:41:07.598677",
        "title": "10% off on a minimum bill amount of Rs. 500",
        "pushType": "0",
        "isLimitedRedeem": "true",
        "couponTag": "1",
        "source": "prime",
        "discountType": "PERCENTAGE_DISCOUNT",
        "merchantGroup": "721",
        "brand": "621",
        "clients[]": ["2", "1"],
        "categories": "2|3|12|11",
        "skuConditionType": "1",
        "skuOfferType": "1",
        "discountPercentageValue": "10",
        "discountMax": "100",
        "discountMinBill": "1000",
        "startDate": "2018/08/06",
        "endDate": "2018/08/31",
        "couponUrl": "https://www.google.com",
        "affiliateUrl": "https://www.google.com",
        "description": "Test Coupons Online and physical both",
        "terms": "Test Coupons Online and physical both",
        "couponLabel": "TESTCoupon",
        "couponCode": "$GENERATE_PER_CUSTOMER",
        "redeemCap": "2",
        "maxRedeem": "200",
        "priv": "0",
        "validFrom": "2018/08/06 00:00:00",
        "validTo": "2018/08/31 23:59:00",
        "redeemHours": "0|24",
        "redeemLocation": "1",
        "reductionType": "1",
        "url": "https://www.google.com",
        "redeem-age-interval": "0|150",
        "status": "APPROVE",
        "subscribe": "true"
    }
}

discount_coupon_list = {
    "file_pull_brand_type_flat_discount_on_sku_discountType":
        {
            'file': ('A.jpg', open(path1 + '/images/A.jpg', 'rb'), 'image/jpeg')
        },
    "data_pull_brand_type_flat_discount_on_sku_discountType":
        {
            "title": "coupon1578492546944",
            "couponLabel": "TESTCoupon",
            "couponType": "2",
            "clients[]": [
                "2",
                "3",
                "7"
            ],
            "source": "discover",
            "pushType": "0",
            "couponTag": "3",
            "discountType": "FLAT_DISCOUNT_WITH_SKU",
            "discountExtraRules": "12",
            "startDate": "2020-01-08",
            "couponStartTime": "2020-01-08T14:09:00.000Z",
            "endDate": "2021-01-07",
            "couponEndTime": "2021-01-07T14:09:00.000Z",
            "imageURL": "/cr/v2/coupons/images/m6PZY1-GYuHgU29tkAoZfg",
            "redeemGender": "OTHER",
            "redeemMinAge": "0",
            "redeemMaxAge": "150",
            "redeemableOnline": "1",
            "couponUrl": "https://www.google.com",
            "affiliateUrl": "https://www.google.com",
            "description": "Test Coupons Online and physical both",
            "terms": "Test Coupons Online and physical both",
            "createTs": "1578498617000",
            "status": "APPROVE",
            "redeemCap": "1000000",
            "maxRedeem": "1000000",
            "merchantRedeemCap": "10000000",
            "couponCode": "$GENERATE_PER_CUSTOMER",
            "isLimitedRedeem": "true",
            "locations": "all",
            "demoCoupon": "0",
            "discountCoupon": "1",
            "discountCouponRadio": "true",
            "perCartRedeem": "1",
            "merchantGroup": "3025",
            "brand": "100922",
            "skuConditionType": "1",
            "skuCondition": "10099666",
            "skuConditionName": "RIN",
            "skuConditionQuantity": "1",
            "skuConditionActualPrice": "121",
            "skuConditionSellingPrice": "115",
            "discountAbsValue": "6",
            "isUniversalCode": "0",
            "redeemDays": "1|2|3|4|5|6|7",
            "redeemMinTime": "0",
            "redeemMaxTime": "24",
            "categories": "20202|30210|30002|70100|70101",
            "priv": "0",
            "validFrom": "2020/01/08 19:39:00",
            "validTo": "2021/01/07 19:39:00",
            "redeemHours": "0|24",
            "redeemLocation": "1",
            "reductionType": "1",
            "url": "https://www.google.com",
            "redeem-age-interval": "0|150",
            "subscribe": "true",
            "userGroup": "42"
        },
    "file_pull_brand_type_Free_SKUs_on_Bill_discountType":
        {
            'file': ('M.jpg', open(path1 + '/images/M.jpg', 'rb'), 'image/jpeg')
        },
    "data_pull_brand_type_Free_SKUs_on_Bill_discountType":
        {
            "redeemDays": "1|2|3|4|5|6|7",
            "redeemMinTime": "0",
            "redeemMaxTime": "24",
            "redeemMinAge": "0",
            "redeemMaxAge": "150",
            "redeemableOnline": "1",
            "isUniversalCode": "0",
            "redeemGender": "MALE",
            "locations": "all",
            "couponType": "2",
            "clients[0]": 1,
            "discountType": "FREE_SKU_WITH_BILL",
            "discountExtraRules": "12",
            "discountAbsValue": "10",
            "skuOffer": "10036387 |10036553",
            "skuOfferName": "Rs.30 off on buying 2 Tide Naturals 800g",
            "skuOfferQuantity": "1",
            "discountMinBill": "100",
            "skuConditionSellingPrice": "110",
            "couponStartTime": "2019-11-28T18:30:00.000Z",
            "couponEndTime": "2022-05-31T18:29:00.000Z",
            "categories": "2|3|12|11",
            "title": "rin_on_100_rs_purchase",
            "pushType": "0",
            "isLimitedRedeem": "true",
            "couponTag": "1",
            "source": "prime",
            "merchantGroup": "581",
            "brand": "99374",
            "startDate": "2019/11/29",
            "endDate": "2022/05/31",
            "couponUrl": "https://www.google.com",
            "affiliateUrl": "https://www.google.com",
            "description": "Test Coupons Online and physical both",
            "terms": "Test Coupons Online and physical both",
            "couponLabel": "TESTCoupon",
            "couponCode": "$GENERATE_PER_CUSTOMER",
            "redeemCap": "10000000",
            "maxRedeem": "10000000",
            "merchantRedeemCap": "10000000",
            "priv": "0",
            "validFrom": "2019/11/29 00:00:00",
            "validTo": "2022/05/31 23:59:00",
            "redeemHours": "0|24",
            "redeemLocation": "1",
            "reductionType": "1",
            "url": "https://www.google.com",
            "redeem-age-interval": "0|150",
            "status": "APPROVE",
            "subscribe": "true",
            "userGroup": "42"

        },
    "file_pull_brand_type_Free_SKUs_on_SKUs_discountType":
        {
            'file': ('C.jpg', open(path1 + '/images/C.jpg', 'rb'), 'image/jpeg')
        },
    "data_pull_brand_type_Free_SKUs_on_SKUs_discountType":
        {
            "title": "1 rin on 1kg ariel",
            "couponLabel": "TESTCoupon",
            "couponType": "2",
            "clients[]": [
                "3",
                "7",
                "2"
            ],
            "source": "prime",
            "pushType": "0",
            "couponTag": "3",
            "discountType": "FREE_SKU_WITH_SKU",
            "discountExtraRules": "12",
            "startDate": "2019-11-29",
            "couponStartTime": "2019-11-28T18:30:00.000Z",
            "endDate": "2022-05-31",
            "couponEndTime": "2022-05-31T18:29:00.000Z",
            "imageURL": "/cr/v2/coupons/images/l,00000001.jpeg",
            "fullImageUrl": "",
            "redeemGender": "MALE",
            "redeemMinAge": "0",
            "redeemMaxAge": "150",
            "redeemableOnline": "1",
            "couponUrl": "https://google.com",
            "affiliateUrl": "https://google.com",
            "description": "Test Coupons Online and physical both",
            "terms": "Test Coupons Online and physical both",
            "createTs": "1578492211000",
            "status": "APPROVE",
            "redeemCap": "10000000",
            "maxRedeem": "10000000",
            "merchantRedeemCap": "10000000",
            "couponCode": "$GENERATE_PER_CUSTOMER",
            "isLimitedRedeem": "true",
            "locations": "all",
            "demoCoupon": "0",
            "discountCoupon": "1",
            "discountCouponRadio": "true",
            "perCartRedeem": "1",
            "merchantGroup": "581",
            "brand": "99374",
            "skuConditionType": "1",
            "skuCondition": "78678876876",
            "skuConditionName": "Pantene Total Damage Control 80ml",
            "skuConditionQuantity": "2",
            "skuConditionActualPrice": "100",
            "skuConditionSellingPrice": "110",
            "isUniversalCode": "0",
            "redeemDays": "1|2|3|4|5|6|7",
            "redeemMinTime": "0",
            "redeemMaxTime": "24",
            "categories": "30210|30002|70100|70101|20002|20202",
            "skuOfferType": "1",
            "skuOffer": "10021580299353",
            "skuOfferName": "RIN",
            "skuOfferQuantity": "1",
            "priv": "0",
            "validFrom": "2019/11/29 00:00:00",
            "validTo": "2022/05/31 23:59:00",
            "redeemHours": "0|24",
            "redeemLocation": "1",
            "reductionType": "1",
            "url": "https://google.com",
            "redeem-age-interval": "0|150",
            "subscribe": "true",
            "userGroup": "42"
        },
    "file_pull_brand_type_Percentage_discount_on_SKU_discountType":
        {
            'file': ('C.jpg', open(path1 + '/images/C.jpg', 'rb'), 'image/jpeg')
        },
    "data_pull_brand_type_Percentage_discount_on_SKU_discountType":
        {
            "title": "coupon1578492546944",
            "couponLabel": "TESTCoupon",
            "couponType": "2",
            "clients[]": [
                "7",
                "2",
                "3"
            ],
            "source": "discover",
            "pushType": "0",
            "couponTag": "3",
            "discountType": "PERCENTAGE_DISCOUNT_WITH_SKU",
            "discountExtraRules": "12",
            "startDate": "2020-01-08",
            "couponStartTime": "2020-01-08T14:09:06.000Z",
            "endDate": "2021-01-07",
            "couponEndTime": "2021-01-07T14:09:06.000Z",
            "redeemGender": "OTHER",
            "redeemMinAge": "0",
            "redeemMaxAge": "150",
            "redeemableOnline": "1",
            "couponUrl": "https://www.google.com",
            "affiliateUrl": "https://www.google.com",
            "description": "Test Coupons Online and physical both",
            "terms": "Test Coupons Online and physical both",
            "createTs": "1578493042000",
            "status": "APPROVE",
            "redeemCap": "1000000",
            "maxRedeem": "1000000",
            "merchantRedeemCap": "10000000",
            "couponCode": "$GENERATE_PER_CUSTOMER",
            "isLimitedRedeem": "true",
            "locations": "all",
            "demoCoupon": "0",
            "discountCoupon": "1",
            "discountCouponRadio": "true",
            "perCartRedeem": "1",
            "merchantGroup": "3025",
            "brand": "100922",
            "isUniversalCode": "0",
            "redeemDays": "1|2|3|4|5|6|7",
            "redeemMinTime": "0",
            "redeemMaxTime": "24",
            "categories": "2|3|20202|30210|30002",
            "categoriesByClient": "[object Object]",
            "discountPercentageValue": "15",
            "discountMax": "15",
            "skuCondition": "10099666871",
            "skuConditionName": "RIN",
            "skuConditionQuantity": "2",
            "skuConditionActualPrice": "100",
            "skuConditionSellingPrice": "115",
            "skuConditionType": "1",
            "priv": "0",
            "validFrom": "2020/01/08 19:39:00",
            "validTo": "2021/01/07 19:39:00",
            "redeemHours": "0|24",
            "redeemLocation": "1",
            "reductionType": "1",
            "url": "https://www.google.com",
            "redeem-age-interval": "0|150",
            "subscribe": "true",
            "userGroup": "42"
        },
    "file_pull_brand_type_Percentage_discount_on_Bill_discountType":
        {
            'file': ('D.jpg', open(path1 + '/images/D.jpg', 'rb'), 'image/jpeg')
        },
    "data_pull_brand_type_Percentage_discount_on_Bill_discountType":
        {
            "redeemDays": "1|2|3|4|5|6|7",
            "redeemMinTime": "0",
            "redeemMaxTime": "24",
            "redeemMinAge": "0",
            "redeemMaxAge": "150",
            "redeemableOnline": "1",
            "isUniversalCode": "0",
            "redeemGender": "MALE",
            "locations": "all",
            "couponType": "2",
            "couponStartTime": "2019-11-28T18:30:00.000Z",
            "couponEndTime": "2022-05-31T18:29:00.000Z",
            "title": "10% off on a minimum bill amount of Rs. 500",
            "pushType": "0",
            "isLimitedRedeem": "true",
            "couponTag": "1",
            "source": "prime",
            "discountType": "PERCENTAGE_DISCOUNT",
            "merchantGroup": "581",
            "brand": "99374",
            "discountCoupon": "1",
            "clients[0]": 2,
            "categories": "2|3|12|11",
            "skuConditionType": "1",
            "skuOfferType": "1",
            "discountPercentageValue": "10",
            "discountMax": "100",
            "discountMinBill": "1000",
            "startDate": "2019/11/29",
            "endDate": "2022/05/31",
            "couponUrl": "https://www.google.com",
            "affiliateUrl": "https://www.google.com",
            "description": "Test Coupons Online and physical both",
            "terms": "Test Coupons Online and physical both",
            "couponLabel": "TESTCoupon",
            "couponCode": "$GENERATE_PER_CUSTOMER",
            "redeemCap": "10000000",
            "maxRedeem": "10000000",
            "merchantRedeemCap": "10000000",
            "priv": "0",
            "validFrom": "2019/11/29 00:00:00",
            "validTo": "2022/05/31 23:59:00",
            "redeemHours": "0|24",
            "redeemLocation": "1",
            "reductionType": "1",
            "url": "https://www.google.com",
            "redeem-age-interval": "0|150",
            "status": "APPROVE",
            "subscribe": "true",
            "userGroup": "42"
        }

}

campaigns_body = {
    'coupon_campaign_creation':
        {
            "name": "coam",
            "startTime": "2020-01-09 00:00:00",
            "endTime": "2020-01-28 23:59:59",
            "lineItems": [
                {
                    "coupons": [
                        "56",
                        "57",
                        "58"
                    ],
                    "segment": {
                        "op": "and",
                        "segments": [
                            {
                                "op": "all",
                                "segments": []
                            }
                        ]
                    }
                }
            ],
            "userGroup": 42
        },
    'coupon_campaign_for_targeting':
        {
            "name": "test",
            "startTime": "2019-04-05 00:00:00",
            "endTime": "2019-04-30 23:59:59",
            "lineItems": [
                {
                    "coupons": [],
                    "segment": {
                        "op": "and",
                        "segments": [
                            {
                                "op": "not",
                                "segments": []
                            }
                        ]
                    }
                },
                {
                    "coupons": [],
                    "segment": {
                        "op": "and",
                        "segments": [
                            {
                                "op": "not",
                                "segments": []
                            }
                        ]
                    }
                }
            ],
        }
}

merchant_body = {
    'file_add_merchants': {
        'image': ('jacoco.png', open(path1 + '/images/C.jpg', 'rb'), 'image/png')
    },

    'data_add_merchants': {
        "traits": "false",
        "isRRMerchant": "false",
        "name": "RR_merchant_bangalore_1",
        "cin": "L12345AA1234AAA123457",
        "url": "https://www.google.com",
        "masId": "ASDPR891999",
        "representative": "JIOMONEY",
        "phone": "9945340313",
        "email": "jiomoney@gmail.com",
        "subscribe": "true",
        "status": "approve",
        "username": "RR_merchant_bangalore_1",
        "userGroup": "42",
        "password": "cee3dc4d010c77d0041bd1e49a39630918559340cc7539d35d318b7f1de8cf02"
    },
    'data_merchant_branch_regular':
        {
            "merchant": '1083',
            "shopNumber": '1',
            "branchCode": 'kormangala',
            "branchName": 'kormangala',
            "zone": "kormangala",
            "state": "kormangala",
            "city": "kormangala",
            "locality": "kormangala",
            "address": "kormangala",
            "landmark": "kormangala",
            "pin": "560034",
            "latitude": "12.77777",
            "longitude": "33.222222",
            "status": "approve"
        },
    'create_merchant_group': {
        "name": "Test_Merchant_group",
        "desc": "Test_Group",
        "idList": [2088, 2089, 2090],
        "userGroup": "42"
    }
}


def assign_coupon_body(couponType):
    choice = {
        'A': ('data_pull_brand_type_flat_discount_on_sku_discountType',
              'file_pull_brand_type_flat_discount_on_sku_discountType'),
        # add_coupon_pull_brand_type_flat_discount_on_sku__or_type
        'B': ('data_pull_brand_type_Free_SKUs_on_Bill_discountType',
              'file_pull_brand_type_Free_SKUs_on_Bill_discountType'),
        # add_coupon_pull_brand_type_Free_SKUs_on_Bill__or_type
        'C': ('data_pull_brand_type_Free_SKUs_on_SKUs_discountType',
              'file_pull_brand_type_Free_SKUs_on_SKUs_discountType'),
        # add_coupon_pull_brand_type_Free_SKUs_on_SKUs__or_type
        'E': ('data_pull_brand_type_Percentage_discount_on_SKU_discountType',
              'file_pull_brand_type_Percentage_discount_on_SKU_discountType'),
        # add_coupon_pull_brand_type_Percentage_discount_on_SKU__or_type
        'F': ('data_pull_brand_type_Percentage_discount_on_Bill_discountType',
              'file_pull_brand_type_Percentage_discount_on_Bill_discountType'),
        # add_coupon_pull_brand_type_Percentage_discount_on_Bill__or_type
        'G': ('data_add_coupon_pull_brand_type_flat_discount_on_sku',
              'file_add_coupon_pull_brand_type_flat_discount_on_sku'),
        # add_coupon_pull_brand_type_flat_discount_on_sku__or_type
        'H': ('data_add_coupon_pull_brand_type_Free_SKUs_on_Bill',
              'file_add_coupon_pull_brand_type_Free_SKUs_on_Bill'),
        # add_coupon_pull_brand_type_Free_SKUs_on_Bill__or_type
        'I': ('data_add_coupon_pull_brand_type_Free_SKUs_on_SKUs',
              'file_add_coupon_pull_brand_type_Free_SKUs_on_SKUs'),
        # add_coupon_pull_brand_type_Free_SKUs_on_SKUs__or_type
        'J': ('data_add_coupon_pull_brand_type_flat_discount',
              'file_add_coupon_pull_brand_type_flat_discount'),  # add_coupon_pull_brand_type_flat_discount
        'K': ('data_add_coupon_pull_brand_type_Percentage_discount_on_SKU',
              'file_add_coupon_pull_brand_type_Percentage_discount_on_SKU'),
        # add_coupon_pull_brand_type_Percentage_discount_on_SKU__or_type
        'L': ('data_add_coupon_pull_brand_type_Percentage_discount_on_Bill',
              'file_add_coupon_pull_brand_type_Percentage_discount_on_Bill'),
        # add_coupon_pull_brand_type_Percentage_discount_on_Bill__or_type
        'M': ('data_brand_type_flat_discount_on_sku_PushType',
              'file_brand_type_flat_discount_on_sku_PushType'),
        'N': ('data_brand_type_Free_SKUs_on_SKUs_PushType',
              'file_brand_type_Free_SKUs_on_SKUs_PushType'),
        'O': ('data_brand_type_Percentage_discount_on_SKU_PushType',
              'file_brand_type_Percentage_discount_on_SKU_PushType'),
    }
    if couponType == 'paymentType':
        foo = ['G', 'I', 'K']  # payment type coupons
        select_coupon = random.choice(foo)
        (data, file) = choice.get(select_coupon)
        return data, file
    elif couponType == 'discountType':
        foo = ['A', 'C', 'E']  # discount type coupons
        select_coupon = random.choice(foo)
        (data, file) = choice.get(select_coupon)
        return data, file
    elif couponType == 'pushType_payment_discount':
        foo = ['M', 'N', 'O']  # push type coupons
        select_coupon = random.choice(foo)
        (data, file) = choice.get(select_coupon)
        return data, file


def assign_merchant_details():
    merchant_details = {
        'A': {
            'image': {'image': ('A.jpg', open(path1 + '/images/A.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "reliance smart"
        },
        'B': {
            'image': {'image': ('B.jpg', open(path1 + '/images/B.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "Ashwarya grocery"
        },
        'C': {
            'image': {'image': ('C.jpg', open(path1 + '/images/C.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "spencer's"
        },
        'D': {
            'image': {'image': ('D.jpg', open(path1 + '/images/D.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "tantra"
        },
        'E': {
            'image': {'image': ('E.jpg', open(path1 + '/images/E.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "mustard"
        },
        'F': {
            'image': {'image': ('F.jpg', open(path1 + '/images/F.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "W"
        },
        'G': {
            'image': {'image': ('G.jpg', open(path1 + '/images/G.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "sony world"
        },
        'H': {
            'image': {'image': ('H.jpg', open(path1 + '/images/H.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "west side"
        },
        'I': {
            'image': {'image': ('I.jpg', open(path1 + '/images/I.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "croma"
        },
        'J': {
            'image': {'image': ('J.jpg', open(path1 + '/images/J.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "spar"
        },
        'K': {
            'image': {'image': ('K.jpg', open(path1 + '/images/K.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "RELIANCE DIGITAL"
        },
        'L': {
            'image': {'image': ('L.jpg', open(path1 + '/images/L.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "lo'real"
        },
        'M': {
            'image': {'image': ('M.jpg', open(path1 + '/images/M.jpg', 'rb'), 'image/jpeg')},
            'merchant_name': "la-femme"
        },

    }

    foo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    return merchant_details.get(random.choice(foo))


def login_to_cms():
    global s
    url = baseURL + "/legacy/login"
    payload = "username=super1&password=c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
    }
    resp = s.post(url, data=payload, headers=headers, verify=False)
    anti_forgery = resp.headers['x-anti-forgery']
    print('logged to CMS', resp, '\n x_antiforge = ', anti_forgery)
    return anti_forgery


def logout_from_cms():
    global s
    global x
    url = baseURL + "/legacy/login"
    headers = {
        "x-anti-forgery": x,
    }
    resp = s.get(url, headers=headers, verify=False)
    print('logged_out from CMS', resp)


def random_char_generator(rang):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(rang))


def coordinate_distributions(city, lat, long, merchant_id, branches_num=1, radius_1=10):
    print("city>>>>>", (city))
    print("merchant_id>>>>>", (merchant_id))
    print("branch_num>>>>>", (branches_num))
    print("given_radius>>>>>", (radius_1))
    a_list, b_list, c_list, d_list, e_list, f_list, g_list, h_list, i_list = [], [], [], [], [], [], [], [], []
    radius = random.randint(1, int(radius_1))  # m - reasonably accurate for distances < 100km
    branches = random.randint(1, int(branches_num))  # varying number of branches in different cities
    center_lat = float(lat)  # latitude of circle center, decimal degrees
    center_lon = float(long)  # Longitude of circle center, decimal degrees
    zone_lst = ["north", "south", "east", "west"]
    print("randomized_radius_value>>>>>>>", radius)
    print("branch_quantity>>>>>>>", branches)
    # generate points
    for k in range(branches):
        c_lat = random.uniform(0.1, 0.09)
        c_lon = random.uniform(0.1, 0.09)
        lat = center_lat + c_lat
        lon = center_lon + c_lon
        pin = random.randint(560001, 831012)
        zone = random.choice(zone_lst)
        a_list.append(merchant_id)  # merchant
        b_list.append(zone)  # zone
        c_list.append(city)  # state
        d_list.append(city)  # city
        e_list.append(city)  # address
        f_list.append(pin)  # pin
        g_list.append(format(float(lat), ".8f"))  # latitude
        h_list.append(format(float(lon), ".8f"))  # latitude
        i_list.append(pin)  # shop_number
    raw_data = {
        'merchant': a_list,
        'zone': b_list,
        'state': c_list,
        'city': d_list,
        'Address': e_list,
        'PIN': f_list,
        'lat': g_list,
        'lng': h_list,
        'shop-number': i_list}
    print("coordinate data>>>>>>>>>>", raw_data)
    df = pd.DataFrame(raw_data)
    random_char = random_char_generator(14)
    with open('{}/files/address_info/address_info_{}.csv'.format(path1, random_char), 'w+') as address_info:
        df.to_csv(address_info, index=False)
    constants["random_char"] = random_char
    del a_list, b_list, c_list, d_list, e_list, f_list, g_list, h_list, df
    return raw_data


def delete_address_info_csv_file():
    rand = constants["random_char"]
    file_path = "{}/files/address_info/address_info_{}.csv".format(path1, rand)
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("The file does not exist")


def delete_address_info():
    new_path = "{}/files/address_info".format(path1)
    if os.path.exists(new_path):
        rmtree(new_path)


def set_mas_id():
    mas_id = (pd.read_csv("{}/files/barcode_data_updated.csv".format(path1))).masID.tolist()
    return mas_id


def update_mas_id_data_merchant(mas_id):
    new_path = "{}/files/barcode_data_updated".format(path1)
    if os.path.exists(new_path):
        rmtree(new_path)
    mas_lst = set_mas_id()
    mas_lst.remove(mas_id)
    created_df = pd.DataFrame(mas_lst, columns=["masID"])
    created_df.to_csv('{}/files/barcode_data_updated.csv'.format(path1), index=False)


def create_merchants(city, lat, long, merchants_num, branches_num, radius_branch):
    mas_id_list = (pd.read_csv("{}/files/barcode_data_updated.csv".format(path1))).masID.tolist()
    url = baseURL + "/v1/cms/admin/merchants"
    header = {
        "x-anti-forgery": x,
        "Content-Type": "application/json"
    }
    for _ in range(int(merchants_num / 1)):
        merchant_list = []
        if merchants_num > 200:
            merchants_num = 200
        # for _ in range(merchants_num):
        for _ in range(1):
            # mas_id = random.sample(setter_getter.get_mas_id_list(), 1)[0]
            mas_id = random.choice(mas_id_list)
            time.sleep(1)

            # Creating merchants
            assign_merchant_details()
            json_data = merchant_body.get("data_add_merchants")
            json_file = assign_merchant_details()['image']
            json_data['masId'] = str(mas_id)
            json_data['name'] = assign_merchant_details()['merchant_name']
            json_data['isRRMerchant'] = random.choice(['true', 'false'])
            json_data['traits'] = random.choice(['true', 'false'])
            json_data = json.dumps(json_data)

            response_full = s.post(url=url,
                                   files=json_file,
                                   data=json_data,
                                   headers=header, verify=False)

            merchant_id = response_full.text
            merchant_list.append(merchant_id)
            merchant_branch = coordinate_distributions(city, lat, long, merchant_id, branches_num, radius_branch)

            # creating branches for the merchants
            json_data = merchant_body.get("data_merchant_branch_regular")
            json_data['merchant'] = str(merchant_branch['merchant'][0])
            json_data['shopNumber'] = str(merchant_branch['shop-number'][0])
            json_data['branchCode'] = str(merchant_branch['shop-number'][0])
            json_data['branchName'] = str(merchant_branch['state'][0])
            json_data['zone'] = str(merchant_branch['zone'][0])
            json_data['state'] = str(merchant_branch['state'][0])
            json_data['city'] = str(merchant_branch['state'][0])
            json_data['locality'] = str(merchant_branch['state'][0])
            json_data['address'] = str(merchant_branch['state'][0])
            json_data['landmark'] = str(merchant_branch['state'][0])
            json_data['pin'] = str(merchant_branch['PIN'][0])
            json_data['latitude'] = str(merchant_branch['lat'][0])
            json_data['longitude'] = str(merchant_branch['lng'][0])
            json_data['status'] = "approve"
            json_data = json.dumps(json_data)

            url = "/v1/cms/merchant/" + merchant_id + '/address'

            header = {
                'x-anti-forgery': x,
                "Content-Type": "application/json"
            }

            s.post(url=url, data=json_data, headers=header, verify=False)

            delete_address_info_csv_file()
            update_mas_id_data_merchant(mas_id)

        # create merchant groups
        json_data = merchant_body.get("create_merchant_group")
        json_data['idList'] = merchant_list
        json_data['name'] = 'merchant_group' + random_char_generator(14)
        json_data['userGroup'] = "42"
        json_data = json.dumps(json_data)
        url = baseURL + "/v1/cms/merchant-group/"
        header = {
            'x-anti-forgery': x,
            "Content-Type": "application/json"
        }
        response_full = s.post(url=url,
                               data=json_data,
                               headers=header,
                               verify=False)

        merchant_group_id = response_full.text()
        merchants_group_id_list.append(json.loads(merchant_group_id)["id"])
    # print("merchants_group_id_list >>>>>>>>>>>>>>", merchants_group_id_list)
    delete_address_info()


def create_campaign_all_segments(coupon_id_list):
    print("____________coupon_id_list_________", coupon_id_list)
    global x
    url = baseURL + "/v1/cms/coupon-campaign/"
    header = {
        "x-anti-forgery": x,
        "Content-Type": "application/json"
    }
    json_data = campaigns_body.get('coupon_campaign_creation')
    json_data['name'] = "Automation_Campaign_" + now.strftime("%Y-%m-%d %H:%M:%S")
    json_data['startTime'] = now.strftime("%Y-%m-%d %H:%M:%S")
    json_data['endTime'] = (now + relativedelta(days=365)).strftime("%Y-%m-%d %H:%M:%S")
    json_data['lineItems'][0]['coupons'] = coupon_id_list
    json_data['userGroup'] = 42
    json_data = json.dumps(json_data)
    print("____________Campaign_Request_Body_________", json_data)
    response_full = s.post(url=url,
                           data=json_data,
                           headers=header, verify=False)
    print("coupon_campaign", response_full.text)


def create_campaign_targeted(coupon_id_list):
    print("____________coupon_id_list_________", coupon_id_list)
    global x
    url = baseURL + "/v1/cms/coupon-campaign/"
    header = {
        'x-anti-forgery': x,
        "Content-Type": "application/json"
    }
    json_data = campaigns_body.get('coupon_campaign_for_targeting')
    json_data["name"] = "Automation_Campaign" + now.strftime("%Y-%m-%d %H:%M:%S")
    json_data["startTime"] = now.strftime("%Y-%m-%d %H:%M:%S")
    json_data["endTime"] = (now + relativedelta(days=365)).strftime("%Y-%m-%d %H:%M:%S")
    json_data['lineItems'][0]['coupons'] = coupon_id_list
    json_data['userGroup'] = 42
    json_data = json.dumps(json_data)
    response_full = s.post(url=url,
                           data=json_data,
                           headers=header, verify=False)
    print("coupon_campaign", response_full.text)


def create_discount_coupons(quantities):
    global x
    global discount_coupon_list
    global campaign
    coupon_id_list = []
    q = quantities // len(mgid)
    for j in mgid:  # for each MGID
        url = baseURL + "/v1/cms/merchant/" + j + "/coupon"
        for i in range(q):  # for each
            data, file = assign_coupon_body('discountType')
            header = {
                'x-anti-forgery': x
            }
            file = discount_coupon_list.get(file)
            json_data = discount_coupon_list.get(data)
            # for _ in json_data.items():
            json_data['couponStartTime'] = datetime.utcnow().isoformat()
            json_data['couponEndTime'] = datetime.utcnow().isoformat()
            json_data['title'] = "coupon1" + str(random_number())
            json_data['merchantGroup'] = j
            json_data['source'] = random.choice(['discover', 'prime'])
            json_data['startDate'] = now.strftime("%Y/%m/%d")
            json_data['endDate'] = (now + relativedelta(days=365)).strftime("%Y/%m/%d")
            json_data["validFrom"] = now.strftime("%Y/%m/%d %H:%M:%S")
            json_data["validTo"] = (now + relativedelta(days=365)).strftime("%Y/%m/%d %H:%M:%S")
            json_data["brand"] = str(random.choice(brand))
            json_data["maxRedeem"] = 1000000
            json_data["redeemCap"] = 1000000
            json_data["merchantRedeemCap"] = 1000000
            json_data["categories"] = "30210|30002|70100|70101|20002|20202",
            json_data["pushType"] = "0"
            json_data["priv"] = "0"
            json_data["discountCoupon"] = "1"
            try:
                if json_data['discountType'] == "FREE_SKU_WITH_SKU":
                    json_data['skuCondition'] = skuid() + "|" + skuid1()
                    json_data['skuConditionName'] = 'Pantene Total Damage Control 80ml'
                    json_data['skuConditionQuantity'] = '2'
                    json_data['skuConditionActualPrice'] = '100'
                    json_data['skuConditionSellingPrice'] = '110'
                    json_data['skuOffer'] = skuid() + "|" + skuid2()
                    json_data['skuOfferName'] = 'RIN'
                    json_data['skuOfferQuantity'] = '1'
                elif json_data['discountType'] == "PERCENTAGE_DISCOUNT_WITH_SKU":
                    json_data['skuCondition'] = skuid() + "|" + skuid1() + "|" + skuid2()
                    json_data['skuConditionName'] = 'RIN'
                    json_data['skuConditionQuantity'] = '2'
                    json_data['skuConditionActualPrice'] = '100'
                    json_data['skuConditionSellingPrice'] = '110'
                    json_data['discountPercentageValue'] = '15'
                    json_data['discountMax'] = '15'
                elif json_data['discountType'] == "FLAT_DISCOUNT_WITH_SKU":
                    json_data['skuCondition'] = skuid()
                    json_data['skuConditionName'] = 'Ariel 1KG'
                    json_data['skuConditionQuantity'] = '1'
                    json_data['skuConditionActualPrice'] = '121'
                    json_data['skuConditionSellingPrice'] = '116'
                    json_data['discountAbsValue'] = '6'
            except KeyError:
                continue
            print("____________discount_coupons_RequestBody_________", json_data)
            response_full = s.post(url=url,
                                   files=file,
                                   data=json_data,
                                   headers=header,
                                   verify=False)
            print("____________discount_coupons_ResponseBody_________", response_full.text)
            coupon_id_list.append(str(json.loads(response_full.text)["id"]))
            if len(coupon_id_list) == campaign:
                create_campaign_all_segments(coupon_id_list)
                # create_campaign_targeted(coupon_id_list)
                coupon_id_list = []


def create_payment_coupons(quantities):
    global x
    global campaign
    coupon_id_list = []
    global payment_type_coupon
    q = quantities // len(mgid)
    for j in mgid:  # for each MGID
        url = baseURL + "/v1/cms/merchant/" + j + "/coupon"
        for i in range(q):
            data, file = assign_coupon_body('paymentType')
            header = {
                'x-anti-forgery': x
            }
            file = payment_type_coupon.get(file)
            json_data = payment_type_coupon.get(data)
            # for _ in json_data.items():
            json_data['couponStartTime'] = datetime.utcnow().isoformat()
            json_data['couponEndTime'] = datetime.utcnow().isoformat()
            json_data['title'] = "coupon1" + str(random_number())
            json_data['merchantGroup'] = j
            json_data['source'] = random.choice(['discover', 'prime'])
            json_data['startDate'] = now.strftime("%Y/%m/%d")
            json_data['endDate'] = (now + relativedelta(days=365)).strftime("%Y/%m/%d")
            json_data["validFrom"] = now.strftime("%Y/%m/%d %H:%M:%S")
            json_data["validTo"] = (now + relativedelta(days=365)).strftime("%Y/%m/%d %H:%M:%S")
            json_data["brand"] = str(random.choice(brand))
            json_data["maxRedeem"] = 1000000
            json_data["redeemCap"] = 1000000
            json_data["merchantRedeemCap"] = 1000000
            json_data["categories"] = "30210|30002|70100|70101|20002|20202",
            json_data["pushType"] = "0"
            json_data["priv"] = "0"
            json_data["discountCoupon"] = "0"
            try:
                if json_data['discountType'] == "FREE_SKU_WITH_SKU":
                    json_data['skuCondition'] = skuid() + "|" + skuid1() + "|" + skuid2()
                    json_data['skuConditionName'] = 'Pantene Total Damage Control 80ml'
                    json_data['skuConditionQuantity'] = '2'
                    json_data['skuConditionActualPrice'] = '100'
                    json_data['skuConditionSellingPrice'] = '110'
                    json_data['skuOffer'] = skuid()
                    json_data['skuOfferName'] = 'RIN'
                    json_data['skuOfferQuantity'] = '1'
                elif json_data['discountType'] == "PERCENTAGE_DISCOUNT_WITH_SKU":
                    json_data['skuCondition'] = skuid() + "|" + skuid1()
                    json_data['skuConditionName'] = 'RIN'
                    json_data['skuConditionQuantity'] = '2'
                    json_data['skuConditionActualPrice'] = '100'
                    json_data['skuConditionSellingPrice'] = '110'
                    json_data['discountPercentageValue'] = '15'
                    json_data['discountMax'] = '15'
                elif json_data['discountType'] == "FLAT_DISCOUNT_WITH_SKU":
                    json_data['skuCondition'] = skuid()
                    json_data['skuConditionName'] = 'Ariel 1KG'
                    json_data['skuConditionQuantity'] = '1'
                    json_data['skuConditionActualPrice'] = '121'
                    json_data['skuConditionSellingPrice'] = '116'
                    json_data['discountAbsValue'] = '6'
            except KeyError:
                continue
            print("____________payment_coupons_RequestBody_________", json_data)
            response_full = s.post(url=url,
                                   files=file,
                                   data=json_data,
                                   headers=header,
                                   verify=False)
            print("____________payment_coupons_ResponseBody_________", response_full.text)
            coupon_id_list.append(json.loads(response_full.text)["id"])
            if len(coupon_id_list) == campaign:
                create_campaign_all_segments(coupon_id_list)
                # create_campaign_targeted(coupon_id_list)
                coupon_id_list = []


def create_push_type_coupons(quantities):
    global x
    global payment_type_coupon
    q = quantities // len(mgid)
    for j in mgid:  # for each MGID
        url = baseURL + "/v1/cms/merchant/" + j + "/coupon"
        for i in range(q):  # for each
            data, file = assign_coupon_body('pushType_payment_discount')
            header = {
                'x-anti-forgery': x
            }
            file = payment_type_coupon.get(file)
            json_data = payment_type_coupon.get(data)
            # for _ in json_data.items():
            json_data['couponStartTime'] = datetime.utcnow().isoformat()
            json_data['couponEndTime'] = datetime.utcnow().isoformat()
            json_data['title'] = "coupon1" + str(random_number())
            json_data['merchantGroup'] = j
            json_data['source'] = random.choice(['discover', 'prime'])
            json_data['startDate'] = now.strftime("%Y/%m/%d")
            json_data['endDate'] = (now + relativedelta(days=365)).strftime("%Y/%m/%d")
            json_data["validFrom"] = now.strftime("%Y/%m/%d %H:%M:%S")
            json_data["validTo"] = (now + relativedelta(days=365)).strftime("%Y/%m/%d %H:%M:%S")
            json_data["brand"] = str(random.choice(brand))
            json_data["maxRedeem"] = 1000000
            json_data["redeemCap"] = 1000000
            json_data["merchantRedeemCap"] = 1000000
            json_data["categories"] = "30210|30002|70100|70101|20002|20202",
            json_data["pushType"] = "1"
            json_data["priv"] = "1"
            json_data["discountCoupon"] = str(random.randint(0, 1))
            try:
                if json_data['discountType'] == "FREE_SKU_WITH_SKU":
                    json_data['skuCondition'] = skuid()
                    json_data['skuConditionName'] = 'Pantene Total Damage Control 80ml'
                    json_data['skuConditionQuantity'] = '2'
                    json_data['skuConditionActualPrice'] = '100'
                    json_data['skuConditionSellingPrice'] = '110'
                    json_data['skuOffer'] = skuid() + "|" + skuid2()
                    json_data['skuOfferName'] = 'RIN'
                    json_data['skuOfferQuantity'] = '1'
                elif json_data['discountType'] == "PERCENTAGE_DISCOUNT_WITH_SKU":
                    json_data['skuCondition'] = skuid() + "|" + skuid1() + "|" + skuid2()
                    json_data['skuConditionName'] = 'RIN'
                    json_data['skuConditionQuantity'] = '2'
                    json_data['skuConditionActualPrice'] = '100'
                    json_data['skuConditionSellingPrice'] = '110'
                    json_data['discountPercentageValue'] = '15'
                    json_data['discountMax'] = '15'
                elif json_data['discountType'] == "FLAT_DISCOUNT_WITH_SKU":
                    json_data['skuCondition'] = skuid() + "|" + skuid1() + "|" + skuid2()
                    json_data['skuConditionName'] = 'Ariel 1KG'
                    json_data['skuConditionQuantity'] = '1'
                    json_data['skuConditionActualPrice'] = '121'
                    json_data['skuConditionSellingPrice'] = '116'
                    json_data['discountAbsValue'] = '6'
            except KeyError:
                continue
            print("____________Push_Coupon_RequestBody_________", json_data)
            response_full = s.post(url=url,
                                   files=file,
                                   data=json_data,
                                   headers=header,
                                   verify=False)
            print("____________Push_Coupon_ResponseBody_________", response_full.text)
            coupon_id = json.loads(response_full.text)["id"]
            # push coupon to numbers
            push_coupon(coupon_id)


def push_coupon(coupon_id):
    phone_number = "9000130" + str(random.randint(100, 600))

    payload = {"phone": phone_number, "couponId": coupon_id}

    payload = json.dumps(payload)
    headers = {
        'Content-Type': "application/json",
    }
    url = baseURL + "/v1/cms/users/coupons/specials"
    print("____________Pushing_coupons_RequestBody_________", payload)
    response_full = requests.post(url=url, data=payload, headers=headers, verify=False)
    print("____________Pushing_coupons_ResponseBody_________", response_full.text)


if __name__ == "__main__":
    x = login_to_cms()
    campaign = 100
    create_discount_coupons(11000)  # 15000
    # create_payment_coupons(5000)     #5000
    # create_push_type_coupons(2000)      #2000
