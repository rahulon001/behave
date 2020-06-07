from features.constants import helpercodes, setter_getter
import pandas as pd
import json, time, random
from datetime import datetime
from features.constants.api_parameters import set_url
from features.constants.api_parameters import set_body
from features.constants.api_parameters import set_headers
from features.constants.api_parameters import set_request
from features.constants.api_parameters import set_parameters

path = setter_getter.get_path()
merchants_group_id_list=[]
coupon_id_list = []
now = datetime.now()


def set_brand_list():
    external_id = (pd.read_csv("{}/files/Brand_ID.csv".format(path))).IDENTITY_FIELD_2.tolist()
    setter_getter.set_brand_external_id_list(external_id)


def set_random_data_list():
    setter_getter.set_brand_external_id_list(helpercodes.create_list_with_random_element(40))


# get brand IDs
def set_existing_brand_list():
    brand_id_lst = []
    setter_getter.set_http_request_type('GET')
    set_url.modify_and_set_url('create_brand')
    set_headers.modify_and_set_headers('multipartFormDataWithAntiForgery')
    set_parameters.modify_and_set_parameters('None')
    set_request.raise_request_multipart_secure('GET')
    for i in range(len(json.loads(setter_getter.get_response_text())["data"])):
        brand_id_lst.append(json.loads(setter_getter.get_response_text())["data"][i]["id"])
    print(brand_id_lst)
    setter_getter.set_brand_id_lst(brand_id_lst)


def set_existing_merchant_group_list():
    setter_getter.set_http_request_type('GET')
    set_url.modify_and_set_url('create_merchant_group')
    set_headers.modify_and_set_headers('multipartFormDataWithAntiForgery')
    set_parameters.modify_and_set_parameters('None')
    set_request.raise_request_multipart_secure('GET')
    for i in range(len(json.loads(setter_getter.get_response_text())["data"])):
        coupon_id_list.append(json.loads(setter_getter.get_response_text())["data"][i]["categories"]["id"])
    print("coupon_id_list =================>",coupon_id_list)
    setter_getter.set_coupon_id_lst(coupon_id_list)


def set_existing_coupon_list():
    setter_getter.set_http_request_type('GET')
    set_url.modify_and_set_url('get_approved_coupon_list')
    set_headers.modify_and_set_headers('multipartFormDataWithAntiForgery')
    set_parameters.modify_and_set_parameters('None')
    set_request.raise_request_multipart_secure('GET')
    for i in range(len(json.loads(setter_getter.get_response_text())["data"])):
        merchants_group_id_list.append(json.loads(setter_getter.get_response_text())["data"][i]["id"])
    print("COUPON_ID_list =================>", merchants_group_id_list)
    setter_getter.set_merchant_grp_id_lst(merchants_group_id_list)


def create_brands(brand_num):
    brand_id_lst = []
    for _ in range(brand_num):
        # helpercodes.login_to_cms()
        # Creating brands
        ext_id = random.sample(setter_getter.get_brand_external_id_list(), 1)[0]
        setter_getter.set_external_id(ext_id)
        brand_creation()
        brand_id = (json.loads(setter_getter.get_response_text()))['id']
        brand_id_lst.append(brand_id)
    print(brand_id_lst)
    setter_getter.set_brand_id_lst(brand_id_lst)


def brand_creation():
    setter_getter.set_http_request_type('POST')
    set_url.modify_and_set_url('create_brand')
    set_body.modify_and_set_data_files('data_create_brand', 'file_create_brand')
    set_headers.modify_and_set_headers('multipartFormDataWithAntiForgery')
    set_request.raise_request_multipart_secure('POST')


def deleting_address_info():
    helpercodes.create_address_info()


def set_mas_id():
    mas_id = (pd.read_csv("{}/files/barcode_data_updated.csv".format(path))).masID.tolist()
    setter_getter.set_mas_id_list(mas_id)


# for brand type coupons
def create_multiple_merchants(city, lat, long, merchants_num, branches_num, radius_branch):
    # for _ in range(int(merchants_num/200)):
    for _ in range(int(merchants_num/1)):
        merchant_list = []
        if merchants_num > 200:
            merchants_num = 200
        # for _ in range(merchants_num):
        for _ in range(1):
            # mas_id = random.sample(setter_getter.get_mas_id_list(), 1)[0]
            mas_id = random.choice(setter_getter.get_mas_id_list())
            print("mas id >>>>>>>>>>>>", mas_id)
            setter_getter.set_mas_id(mas_id)
            time.sleep(1)

            # Creating merchants
            creating_merchant()
            setter_getter.set_merchant_id(setter_getter.get_response_text())
            merchant_list.append(setter_getter.get_response_text())
            helpercodes.coordinate_distributions(city, lat, long, setter_getter.get_response_text(), branches_num,
                                                 radius_branch)

            # creating branches for the merchants
            merchant_branch()
            helpercodes.delete_address_info_csv_file()
            update_mas_id_data_merchant(mas_id)

        setter_getter.set_merchant_list(merchant_list)
        create_merchant_group()      # create merchant groups
        t = (setter_getter.get_response_text())
        merchants_group_id_list.append(json.loads(t)["id"])
    # print("merchants_group_id_list >>>>>>>>>>>>>>", merchants_group_id_list)

    setter_getter.set_merchant_grp_id_lst(merchants_group_id_list)
    helpercodes.delete_address_info()


# for merchant type coupons
# def create_multiple_merchants(city, lat, long, merchants_num, branches_num, radius_branch):
#     merchant_list = []
#     for _ in range(merchants_num):
#         helpercodes.login_to_cms()
#         mas_id = random.sample(setter_getter.get_mas_id_list(), 1)[0]
#         print("mas id >>>>>>>>>>>>", mas_id)
#         setter_getter.set_mas_id(mas_id)
#         time.sleep(1)
#
#         # Creating merchants
#         creating_merchant()
#         setter_getter.set_merchant_id(setter_getter.get_response_text())
#         merchant_list = helpercodes.merchant_lst(setter_getter.get_response_text())
#         print("merchant list >>>>>>>", merchant_list)
#         helpercodes.coordinate_distributions(city, lat, long, setter_getter.get_response_text(), branches_num,
#                                                  radius_branch)
#
#         # creating branches for the merchants
#         merchant_branch()
#
#         update_mas_id_data_merchant(mas_id)
#     setter_getter.set_merchant_list(merchant_list)
#     helpercodes.delete_address_info()


def merchant_branch():
    set_body.modify_and_set_data_files('data_merchant_branch_regular', None)
    setter_getter.set_http_request_type('POST')
    set_url.modify_and_set_url('add_merchant_branch_regular')
    set_headers.modify_and_set_headers('multipartFormDataWithAntiForgery')
    set_request.raise_request_multipart_secure('POST')


def update_mas_id_data_merchant(mas_id):
    helpercodes.delete_masID()
    mas_lst = setter_getter.get_mas_id_list()
    mas_lst.remove(mas_id)
    created_df = pd.DataFrame(mas_lst, columns=["masID"])
    created_df.to_csv('{}/files/barcode_data_updated.csv'.format(path), index=False)


def creating_merchant():
    set_body.modify_and_set_data_files('data_add_merchants', 'file_add_merchants')
    setter_getter.set_http_request_type('POST')
    set_url.modify_and_set_url('add_merchant')
    set_headers.modify_and_set_headers('multipartFormDataWithAntiForgery')
    set_request.raise_request_multipart_secure('POST')


def create_merchant_group():
    # helpercodes.login_to_cms()
    set_body.modify_and_set_data_files('create_merchant_group', None, setter_getter.get_merchant_list())
    set_url.modify_and_set_url('create_merchant_group')
    set_headers.modify_and_set_headers('secureJson')
    set_request.raise_request_multipart_secure('POST')


# for creating brand type coupon
def create_multiple_coupons(coupon_num):
    coupon_id_lst = []
    sku_list = []
    # for _ in range(int(coupon_num/250)):
    for _ in range(int(coupon_num/50)):
        if coupon_num > 200:
            coupon_num = 200
        for _ in range(coupon_num):
            setter_getter.set_merchant_grp_id(random.choice(setter_getter.get_merchant_grp_id_lst()))
            ran_1 = random.randint(2,6)
            random_sku = helpercodes.random_sku_(ran_1)
            print("<<<<SKU_ID>>>>", random_sku)
            sku_list.append(random_sku)
            setter_getter.set_sku_id(random_sku)
            # helpercodes.login_to_cms()
            set_headers.modify_and_set_headers("multipartFormDataWithAntiForgery")
            data, file, url = helpercodes.assign_coupon_body()
            # print("merchant_list", (setter_getter.get_merchant_list())[0])
            # print("merchant_group_id", (setter_getter.get_merchant_grp_id()))
            set_url.modify_and_set_url(url)
            set_body.modify_and_set_data_files(data, file)
            set_request.raise_request_multipart_secure('POST')
            coupon_id = (json.loads(setter_getter.get_response_text()))['id']
            coupon_id_lst.append(coupon_id)
        setter_getter.set_coupon_list(coupon_id_lst)
        print("coupon_id_list", coupon_id_lst)
        # create_campaigns()
        coupon_id_lst = []
    print("<<sku_id_lst>>",sku_list)
    setter_getter.set_sku_list(sku_list)


def create_multiple_coupons_for_targeting(coupon_num):
    coupon_id_lst = []
    sku_list = []
    # for _ in range(int(coupon_num/250)):
    for _ in range(int(coupon_num/3)):
        if coupon_num > 200:
            coupon_num = 200
        for _ in range(coupon_num):
            setter_getter.set_merchant_grp_id(random.choice(setter_getter.get_merchant_grp_id_lst()))
            random_sku = random.randint(8000, 10000)
            print("<<<<SKU_ID>>>>", random_sku)
            sku_list.append(random_sku)
            setter_getter.set_sku_id(random_sku)
            # helpercodes.login_to_cms()
            set_headers.modify_and_set_headers("multipartFormDataWithAntiForgery")
            data, file, url = helpercodes.assign_coupon_body()
            print("merchant_list", (setter_getter.get_merchant_list())[0])
            print("merchant_group_id", (setter_getter.get_merchant_grp_id()))
            set_url.modify_and_set_url(url)
            set_body.modify_and_set_data_files(data, file)
            set_request.raise_request_multipart_secure('POST')
            coupon_id = (json.loads(setter_getter.get_response_text()))['id']
            coupon_id_lst.append(coupon_id)
        setter_getter.set_coupon_list(coupon_id_lst)
        print("coupon_id_list",coupon_id_lst)
        create_campaigns_for_targeting()
        coupon_id_lst = []
    print("<<sku_id_lst>>",sku_list)
    setter_getter.set_sku_list(sku_list)

# for creating merchant type coupon
# def create_multiple_coupons(coupon_num):
#     coupon_id_lst = []
#     sku_list = []
#     # for _ in range(int(coupon_num/250)):
#     for _ in range(int(coupon_num/5)):
#         if coupon_num > 200:
#             coupon_num = 200
#         for _ in range(coupon_num):
#             random_sku = random.randint(8000, 10000)
#             print("<<<<SKU_ID>>>>", random_sku)
#             sku_list.append(random_sku)
#             setter_getter.set_sku_id(random_sku)
#             helpercodes.login_to_cms()
#             set_headers.modify_and_set_headers("multipartFormDataWithAntiForgery")
#             data, file, url = helpercodes.assign_coupon_body()
#             print("merchant_list", (setter_getter.get_merchant_list())[0])
#             set_url.modify_and_set_url(url)
#             set_body.modify_and_set_data_files(data, file)
#             set_request.raise_request_multipart_secure('POST')
#             coupon_id = (json.loads(setter_getter.get_response_text()))['id']
#             coupon_id_lst.append(coupon_id)
#         setter_getter.set_coupon_list(coupon_id_lst)
#         print("coupon_id_list",coupon_id_lst)
#         create_campaigns()
#         coupon_id_lst = []
#     print("<<sku_id_lst>>",sku_list)
#     setter_getter.set_sku_list(sku_list)


def create_campaigns():
    set_body.modify_and_set_data_files('couponCampaignCreation', None, setter_getter.get_coupon_list())
    set_url.modify_and_set_url('couponCampaignCreation')
    set_headers.modify_and_set_headers('secureJson')
    set_request.raise_request_multipart_secure('POST')


def assign_verify_user_to_coupon(coupon_code_quantity):
    for i in setter_getter.get_coupon_list():
        k, l = 0, 0
        coupon_code_lst = []
        sku_id_list_rr = []
        setter_getter.set_user_numbers(random.randint(9941240312, 9949240311))
        print("<<<<user number >>>>", setter_getter.get_user_numbers())
        # sku_id = setter_getter.get_sku_list()[k]
        # print("*****SKU_ID*****",sku_id)
        # setter_getter.set_sku_id(sku_id)
        k += 1
        for _ in range(coupon_code_quantity):
            # Assign coupon to user
            print("<<<<<<step1>>>>>>")
            set_url.modify_and_set_url('couponCodeDistributionAPI', i)
            set_body.modify_and_set_simple_body('couponCodeDistributionAPI')
            set_headers.modify_and_set_headers('couponCodeDistributionAPI')
            set_parameters.modify_and_set_parameters('couponCodeDistributionAPI')
            set_request.raise_request_with_parameters('POST')
            if "redeemCode" in json.loads(setter_getter.get_response_text()):
                setter_getter.set_redeem_code(json.loads(setter_getter.get_response_text())["redeemCode"])
            else:
                continue
            # determine best coupons for the discount
            print("<<<<<<step2>>>>>>")
            set_url.modify_and_set_url('cart_redeem')
            set_body.modify_and_set_simple_body('cart_redeem')
            set_headers.modify_and_set_headers('applicationJson')
            set_request.request_raise('POST')
            # verify coupon code for merchant
            for _ in json.loads(setter_getter.get_response_text())['skuCoupons']:
                try:
                    if json.loads(setter_getter.get_response_text())['skuCoupons'][l]['coupons'][0]['couponCode']:
                        print("<<<Sku id from remote redemption>>>", json.loads(setter_getter.get_response_text())['skuCoupons'][l]['skuId'])
                        print("<<<<coupon code from remote redemption>>>>", json.loads(setter_getter.get_response_text())['skuCoupons'][l]['coupons'][0]['couponCode'])
                        coupon_code_lst.append(str(json.loads(setter_getter.get_response_text())['skuCoupons'][l]['coupons'][0]['couponCode']))
                        sku_id_list_rr.append(str(json.loads(setter_getter.get_response_text())['skuCoupons'][l]['skuId']))
                        l += 1
                except IndexError:
                    continue
            print("<<<coupon code list >>>", coupon_code_lst)
            print("<<<sku id list >>>", sku_id_list_rr)
            setter_getter.set_coupon_code_lst(coupon_code_lst)
            setter_getter.set_sku_id_list_rr(sku_id_list_rr)
            for j in range(len(setter_getter.get_sku_id_list_rr())):
                for i in range(len(setter_getter.get_coupon_code_lst())):
                    print("<<<<<<step3>>>>>>")
                    set_url.modify_and_set_url('merchant_verify')
                    set_body.modify_and_set_simple_body('merchant_verify', i , j)
                    set_headers.modify_and_set_headers('merchant_verify')
                    set_request.request_raise('POST')
                    # checkout coupon code
                    print("<<<<<<step4>>>>>>")
                    set_url.modify_and_set_url('checkout_coupon_code')
                    set_body.modify_and_set_simple_body('checkout_coupon_code', i, j)
                    set_headers.modify_and_set_headers('merchant_verify')
                    set_request.raise_request_with_parameters('POST')
                    # redeem coupon code for merchant
                    print("<<<<<<step5>>>>>>")
                    set_url.modify_and_set_url('merchant_redeem')
                    set_body.modify_and_set_simple_body('merchant_redeem', i, j)
                    set_headers.modify_and_set_headers('merchant_redeem')
                    set_request.raise_request_with_parameters('POST')


def create_promo(num):
    promo_lst = []
    for i in range(num):
        setter_getter.set_http_request_type('POST')
        set_url.modify_and_set_url('couponRetailPromoCreation')
        set_headers.modify_and_set_headers('applicationJson')
        set_body.modify_and_set_simple_body('CreatePromoRelianceRetail')
        set_request.request_raise('POST')
        promo_lst.append(setter_getter.get_random_num_generator())
        setter_getter.set_promo_list(promo_lst)


def create_segments(segment_number):
    segment_list = []
    segment_id_list = []
    setter_getter.set_value(segment_number)
    for i in range(segment_number):
        setter_getter.set_http_request_type('POST')
        set_url.modify_and_set_url('create_segment')
        set_headers.modify_and_set_headers('secureJson')
        set_body.modify_and_set_data_files('create_segment', None)
        segment_list.append(setter_getter.get_random_char_generator())
        set_request.raise_request_multipart_secure('POST')
        segment_id_list.append((json.loads(setter_getter.get_response_text()))["id"])
    print("<<<<<<Segment_list>>>>>>", segment_list)
    print("<<<<<<segment_CMS_id>>>>>>", segment_id_list)
    setter_getter.set_segment_list(segment_list)
    setter_getter.set_segment_CMS_id(segment_id_list)


def link_user_to_segments(user_quantity):
    for _ in range(user_quantity):
        k = random.randint(2, setter_getter.get_value())
        user = str(random.randint(7949240311, 9941240312))
        segments = ",".join(str(elements) for elements in random.sample(setter_getter.get_segment_list(), k))
        print("segments", segments)
        format_to_insert_in_ignite = [user, '1001', segments, now.strftime("%d-%m-%Y %H:%M:%S")]
        print(tuple(format_to_insert_in_ignite))


def create_multiple_coupons_along_with_all_entities(city, lat, long, merchants_num, branches_num, radius_branch, num):
    set_existing_brand_list()
    deleting_address_info()
    set_mas_id()
    create_multiple_merchants(city, lat, long, merchants_num, branches_num, radius_branch)
    create_multiple_coupons_for_targeting(num)


def create_campaigns_for_targeting():
    c_list = setter_getter.get_coupon_list()
    coupon_quantity = len(setter_getter.get_coupon_list())
    chunk = [c_list[l:l + 5] for l in range(0, coupon_quantity, 5)]
    print("========couponList_chunk", chunk)
    for i in chunk:
        setter_getter.set_coupon_list_chunk(i)
        set_body.modify_and_set_data_files('coupon_campaign_for_targeting', None)
        set_url.modify_and_set_url('couponCampaignCreation')
        set_headers.modify_and_set_headers('secureJson')
        set_request.raise_request_multipart_secure('POST')