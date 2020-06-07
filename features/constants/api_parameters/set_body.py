# Created By Rahul Ranjan on 26/08/2018.

import json
import random
from datetime import datetime
from features.constants import helpercodes, setter_getter
from features.constants.apiBody import apiBodyDict
from dateutil.relativedelta import relativedelta

path = setter_getter.get_path()
now = datetime.now()
constants = {}


def modify_and_set_simple_body(data, *args):
    request_type = setter_getter.get_http_request_type()
    constants['coupon_details'] = helpercodes.assig_coupon_details()
    if data == 'CreatePromoRelianceRetail':
        promo_lst = []
        json_body = apiBodyDict.get(data)
        json_data = json_body['promotions'][0]
        for key, value in json_data.items():
            if key == "REF_ID" and request_type == 'POST':
                setter_getter.set_random_num_generator(6898, 9778966779)
                promo_lst.append(setter_getter.get_random_num_generator())
                setter_getter.set_promo_list(promo_lst)
                json_data["REF_ID"] = str(setter_getter.get_random_num_generator())
                json_data["PROMO_NAME"] = constants['coupon_details']['name']
                json_data["PROMO_CREATION_DATE"] = now.strftime("%Y-%m-%d %H:%M:%S")
                json_data["START_DATE"] = now.strftime("%Y-%m-%d %H:%M:%S")
                json_data["END_DATE"] = (now + relativedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
                json_data["ENTITY"][0]['NAME'] = constants['coupon_details']['name1']
                json_data["ENTITY"][0]['CATEGORIES'] = constants['coupon_details']['category']
                json_data["STORE_ID"] = constants['coupon_details']['Merchant']
            elif key == "REF_ID" and request_type == 'PUT':
                break
        constants['api_Body'] = json.dumps(json_body, ensure_ascii=False)
    elif data == 'merchant_verify':
        json_body = apiBodyDict.get(data)
        for _ in json_body.items():
            json_body["masId"] = constants['masID']
            json_body["storeId"] = constants['masID']
            json_body["couponCodes"] = setter_getter.get_coupon_code_lst()[args[0]]
            json_body['skuData'][args[0]]['skuId'] = setter_getter.get_sku_id_list_rr()[args[1]]
            json_body['skuData'][args[0]]['skuQty'] = 1
            json_body['skuData'][args[0]]['skuPrice'] = 10
            json_body['billAmount'] = 100
        constants['api_Body'] = json.dumps(json_body, ensure_ascii=False)
    elif data == "checkout_coupon_code":
        json_body = apiBodyDict.get(data)
        for _ in json_body.items():
            json_body["masId"] = constants['masID']
            json_body["storeId"] = constants['masID']
            json_body["mId"] = constants['masID']
            json_body["couponCodes"] = setter_getter.get_coupon_code_lst()[args[0]]
            json_body['skuData'][args[0]]['skuId'] = setter_getter.get_sku_id_list_rr()[args[1]]
            json_body['skuData'][args[0]]['skuQty'] = 1
            json_body['skuData'][args[0]]['skuPrice'] = 10
            json_body['billAmount'] = 100
            constants['api_Body'] = json.dumps(json_body, ensure_ascii=False)
    elif data == "cart_redeem":
        i = 1
        json_body = apiBodyDict.get(data)
        json_body['phone'] = setter_getter.get_user_numbers()
        json_body['masId'] = constants['masID']
        json_body['skuData'][0]['skuId'] = setter_getter.get_sku_id()
        json_body['skuData'][0]['skuQty'] = 1
        json_body['skuData'][0]['skuPrice'] = 10
        for _ in json_body['skuData']:
            try:
                if json_body['skuData'][i]['skuId']:
                    sku = random.choice(setter_getter.get_sku_list())
                    json_body['skuData'][i]['skuId'] = str(sku)
                    json_body['skuData'][i]['skuQty'] = 1
                    json_body['skuData'][i]['skuPrice'] = 10
                    i += 1
            except IndexError:
                break
        json_body['billAmount'] = 100
        constants['api_Body'] = json.dumps(json_body, ensure_ascii=False)
    elif data == "merchant_redeem":
        json_body = apiBodyDict.get(data)
        for _ in json_body.items():
            json_body["masId"] = constants['masID']
            json_body["couponCodes"] = setter_getter.get_coupon_code_lst()[args[0]]
            json_body["storeId"] = constants['masID']
        constants['api_Body'] = json.dumps(json_body, ensure_ascii=False)
    else:
        body = apiBodyDict.get(data)
        constants['api_Body'] = body
    setter_getter.set_body(constants['api_Body'])


def modify_and_set_data_files(data, file, *args):
    constants['coupon_details'] = helpercodes.assig_coupon_details()
    # setter_getter.set_sku_details(helpercodes.assign_sku_detail())
    if data == "data_convertPromoToCoupon" and file == "file_convertPromoToCoupon":
        constants['api_file_multipart'] = constants['coupon_details']['image']
        constants['api_data_multipart1'] = apiBodyDict.get(data)
        constants['api_data_multipart1']['promoList[]'] = setter_getter.get_promo_list()
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(constants['api_data_multipart1'])
    elif file == "mapCouponCodeToPromo":
        helpercodes.create_couponcode_redeem_file(setter_getter.get_promo_list())
        constants['api_file_multipart'] = apiBodyDict.get(file)
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(None)
    elif file == "redeemCoupon":
        constants['api_file_multipart'] = apiBodyDict.get(file)
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(None)
    elif data == 'couponCampaignCreation':
        json_data = apiBodyDict.get(data)
        for _ in json_data.items():
            json_data["name"] = "Automation_Campaign"+now.strftime("%Y-%m-%d %H:%M:%S")
            json_data["startTime"] = now.strftime("%Y-%m-%d %H:%M:%S")
            json_data["endTime"] = (now + relativedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S")
            json_data['lineItems'][0]['coupons'] = setter_getter.get_coupon_list()
            json_data['userGroup'] = "42"
        constants['api_data_multipart1'] = json.dumps(json_data, ensure_ascii=False)
        setter_getter.set_file(None)
        setter_getter.set_data(constants['api_data_multipart1'])
    elif data == 'coupon_campaign_for_targeting':
        json_data = apiBodyDict.get(data)
        print("=============json_data======", json_data)
        segment_list = setter_getter.get_segment_CMS_id()
        print("=========get_coupon_list_chunk", setter_getter.get_coupon_list_chunk())
        d = random.randint(1, 2)
        segment_chunk = random.sample([segment_list[l:l + d] for l in range(0, len(segment_list), d)], 4)
        print("=========get_segment_list_chunk", segment_chunk)
        ls = len(segment_chunk)
        try:
            for i in range(-ls, -1, 1):
                json_data['lineItems'][0]['segment']['segments'][i] = str(segment_chunk[0][i])
                json_data['lineItems'][1]['segment']['segments'][i] = str(segment_chunk[2][i])
        except IndexError:
            pass
        for _ in json_data.items():
            json_data["name"] = "Automation_Campaign_targeting" + now.strftime("%Y-%m-%d %H:%M:%S")
            json_data["startTime"] = now.strftime("%Y-%m-%d %H:%M:%S")
            json_data["endTime"] = (now + relativedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S")
            json_data['lineItems'][0]['coupons'] = setter_getter.get_coupon_list_chunk()
            json_data['lineItems'][1]['coupons'] = setter_getter.get_coupon_list_chunk()
            json_data['lineItems'][0]['segment']['segments'][-1]['segments'] = segment_chunk[1]
            json_data['lineItems'][1]['segment']['segments'][-1]['segments'] = segment_chunk[3]
        json_data['userGroup'] = "42"
        constants['api_data_multipart1'] = json.dumps(json_data, ensure_ascii=False)
        setter_getter.set_file(None)
        setter_getter.set_data(constants['api_data_multipart1'])
    elif data == "data_add_merchants" and file == "file_add_merchants":
        constants['merchant_details'] = helpercodes.assig_merchant_details()
        json_data = apiBodyDict.get(data)
        setter_getter.set_random_char_generator(14)
        constants['api_file_multipart'] = constants['merchant_details']['image']
        constants['masID'] = setter_getter.get_mas_id()
        for _ in json_data.items():
            json_data['masId'] = str(constants['masID'])
            json_data['name'] = constants['merchant_details']['merchant_name']
            json_data['isRRMerchant'] = random.choice(['true', 'false'])
            json_data['traits'] = random.choice(['true', 'false'])
        constants['api_data_multipart1'] = json_data
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(constants['api_data_multipart1'])
    elif data == 'data_add_branches' and file == 'file_add_branches':
        json_file = apiBodyDict.get(file)
        rand = setter_getter.get_random_char_generator()
        l = list(json_file['file'])
        l[0] = 'address_info{}.csv'.format(rand)
        l[1] = open('{}/files/address_info/address_info_{}.csv'.format(path, rand), 'rb')
        json_file = {'file': tuple(l)}
        constants['api_file_multipart'] = json_file
        constants['api_data_multipart1'] = apiBodyDict.get('data_add_branches')
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(constants['api_data_multipart1'])
    elif data == 'data_merchant_branch_regular' and file == None:
        json_data = apiBodyDict.get(data)
        json_data['merchant'] = str(setter_getter.get_merchant_branch_data()['merchant'][0])
        json_data['shopNumber'] = str(setter_getter.get_merchant_branch_data()['shop-number'][0])
        json_data['branchCode'] = str(setter_getter.get_merchant_branch_data()['shop-number'][0])
        json_data['branchName'] = str(setter_getter.get_merchant_branch_data()['state'][0])
        json_data['zone'] = str(setter_getter.get_merchant_branch_data()['zone'][0])
        json_data['state'] = str(setter_getter.get_merchant_branch_data()['state'][0])
        json_data['city'] = str(setter_getter.get_merchant_branch_data()['state'][0])
        json_data['locality'] = str(setter_getter.get_merchant_branch_data()['state'][0])
        json_data['address'] = str(setter_getter.get_merchant_branch_data()['state'][0])
        json_data['landmark'] = str(setter_getter.get_merchant_branch_data()['state'][0])
        json_data['pin'] = str(setter_getter.get_merchant_branch_data()['PIN'][0])
        json_data['latitude'] = str(setter_getter.get_merchant_branch_data()['lat'][0])
        json_data['longitude'] = str(setter_getter.get_merchant_branch_data()['lng'][0])
        json_data['status'] = "approve"
        constants['api_data_multipart1'] = json_data
        setter_getter.set_file(None)
        setter_getter.set_data(constants['api_data_multipart1'])

    elif(
            data == "data_add_coupon_pull_merchant_type_flat_discount_on_sku" and
            file == "file_add_coupon_pull_merchant_type_flat_discount_on_sku") or \
            (
                    data == "data_add_coupon_pull_merchant_type_Free_SKUs_on_Bill" and
                    file == "file_add_coupon_pull_merchant_type_Free_SKUs_on_Bill") or \
            (
                    data == "data_add_coupon_pull_merchant_type_Free_SKUs_on_SKUs" and
                    file == "file_add_coupon_pull_brand_type_Free_SKUs_on_SKUs") or \
            (
                    data == "data_add_coupon_pull_merchant_type_flat_discount" and
                    file == "file_add_coupon_pull_merchant_type_flat_discount") or \
            (
                    data == "data_add_coupon_pull_merchant_type_Percentage_discount_on_SKU" and
                    file == "file_add_coupon_pull_merchant_type_Percentage_discount_on_SKU") or \
            (
                    data == "data_add_coupon_pull_merchant_type_Percentage_discount_on_Bill" and
                    file == "file_add_coupon_pull_merchant_type_Percentage_discount_on_Bill"):

        json_data = apiBodyDict.get(data)
        constants['coupon_details'] = helpercodes.assig_coupon_details()
        constants['api_file_multipart'] = constants['coupon_details']['image']
        for _ in json_data.items():
            json_data['couponStartTime'] = datetime.utcnow().isoformat()
            json_data['couponEndTime'] = datetime.utcnow().isoformat()
            json_data['title'] = constants['coupon_details']['name']
            json_data['merchant'] = setter_getter.get_merchant_list()[0]
            json_data['source'] = random.choice(['discover', 'prime'])
            json_data['startDate'] = now.strftime("%Y/%m/%d")
            json_data['endDate'] = (now + relativedelta(days=1)).strftime("%Y/%m/%d")
            json_data["validFrom"] = now.strftime("%Y/%m/%d %H:%M:%S")
            json_data["validTo"] = (now + relativedelta(days=20)).strftime("%Y/%m/%d %H:%M:%S")
            json_data["maxRedeem"] = 1000000
            json_data["redeemCap"] = 100000
            json_data["validTo"] = (now + relativedelta(days=1)).strftime("%Y/%m/%d %H:%M:%S")
            json_data["maxRedeem"] = 100000
            json_data["redeemCap"] = 1000
            json_data["categories"] = str(setter_getter.get_category_id())
            json_data["pushType"] = "0"
            json_data['userGroup'] = "42"
            try:
                if json_data['skuConditionQuantity']:
                    json_data['skuConditionQuantity'] = '1'
                if json_data['skuConditionActualPrice']:
                    json_data['skuConditionActualPrice'] = '5'
                if json_data['skuConditionSellingPrice']:
                    json_data['skuConditionActualPrice'] = '10'
                if json_data['skuCondition']:
                    json_data['skuCondition'] = str(setter_getter.get_sku_id())
            except KeyError:
                continue
        constants['api_data_multipart1'] = json_data
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(constants['api_data_multipart1'])
    elif(
            data == "data_add_coupon_pull_brand_type_flat_discount_on_sku" and
            file == "file_add_coupon_pull_brand_type_flat_discount_on_sku") or \
            (
                    data == "data_add_coupon_pull_brand_type_Free_SKUs_on_SKUs" and
                    file == "file_add_coupon_pull_brand_type_Free_SKUs_on_SKUs") or \
            (
                    data == "data_add_coupon_pull_brand_type_Free_SKUs_on_Bill" and
                    file == "file_add_coupon_pull_brand_type_Free_SKUs_on_Bill") or \
            (
                    data == "data_add_coupon_pull_brand_type_flat_discount" and
                    file == "file_add_coupon_pull_brand_type_flat_discount") or \
            (
                    data == "data_add_coupon_pull_brand_type_Percentage_discount_on_SKU" and
                    file == "file_add_coupon_pull_brand_type_Percentage_discount_on_SKU") or \
            (
                    data == "data_add_coupon_pull_brand_type_Percentage_discount_on_Bill" and
                    file == "file_add_coupon_pull_brand_type_Percentage_discount_on_Bill"):

        json_data = apiBodyDict.get(data)
        constants['coupon_details'] = helpercodes.assig_coupon_details()
        constants['api_file_multipart'] = constants['coupon_details']['image']
        for _ in json_data.items():
            json_data['couponStartTime'] = datetime.utcnow().isoformat()
            json_data['couponEndTime'] = datetime.utcnow().isoformat()
            json_data['title'] = constants['coupon_details']['name']
            json_data['merchantGroup'] = setter_getter.get_merchant_grp_id()
            json_data['source'] = random.choice(['discover', 'prime'])
            json_data['startDate'] = now.strftime("%Y/%m/%d")
            json_data['endDate'] = (now + relativedelta(days=1)).strftime("%Y/%m/%d")
            json_data["validFrom"] = now.strftime("%Y/%m/%d %H:%M:%S")
            json_data["validTo"] = (now + relativedelta(days=1)).strftime("%Y/%m/%d %H:%M:%S")
            json_data["brand"] = random.choice(setter_getter.get_brand_id_lst())
            json_data["maxRedeem"] = 1000000
            json_data["redeemCap"] = 100000
            json_data["categories"] = str(setter_getter.get_category_id())
            json_data["pushType"] = "0"
            try:
                if json_data['skuConditionQuantity']:
                    json_data['skuConditionQuantity'] = '1'
                if json_data['skuConditionActualPrice']:
                    json_data['skuConditionActualPrice'] = '5'
                if json_data['skuConditionSellingPrice']:
                    json_data['skuConditionActualPrice'] = '10'
                if json_data['skuCondition']:
                    json_data['skuCondition'] = str(setter_getter.get_sku_id())
            except KeyError:
                continue
        constants['api_data_multipart1'] = json_data
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(constants['api_data_multipart1'])
    elif(
            data == "data_add_coupon_push_brand_type_flat_discount_on_sku" and
            file == "file_add_coupon_push_brand_type_flat_discount_on_sku") or \
            (
                    data == "data_add_coupon_push_brand_type_Free_SKUs_on_SKUs" and
                    file == "file_add_coupon_push_brand_type_Free_SKUs_on_SKUs") or \
            (
                    data == "data_add_coupon_push_brand_type_Free_SKUs_on_Bill" and
                    file == "file_add_coupon_push_brand_type_Free_SKUs_on_Bill") or \
            (
                    data == "data_add_coupon_push_brand_type_flat_discount" and
                    file == "file_add_coupon_push_brand_type_flat_discount") or \
            (
                    data == "data_add_coupon_push_brand_type_Percentage_discount_on_SKU" and
                    file == "file_add_coupon_push_brand_type_Percentage_discount_on_SKU") or \
            (
                    data == "data_add_coupon_push_brand_type_Percentage_discount_on_Bill" and
                    file == "file_add_coupon_push_brand_type_Percentage_discount_on_Bill"):

        json_data = apiBodyDict.get(data)
        constants['coupon_details'] = helpercodes.assig_coupon_details()
        constants['api_file_multipart'] = constants['coupon_details']['image']
        for _ in json_data.items():
            json_data['couponStartTime'] = datetime.utcnow().isoformat()
            json_data['couponEndTime'] = datetime.utcnow().isoformat()
            json_data['title'] = constants['coupon_details']['name']
            json_data['merchantGroup'] = setter_getter.get_merchant_grp_id()
            json_data['source'] = random.choice(['discover', 'prime'])
            json_data['startDate'] = now.strftime("%Y/%m/%d")
            json_data['endDate'] = (now + relativedelta(days=10)).strftime("%Y/%m/%d")
            json_data["validFrom"] = now.strftime("%Y/%m/%d %H:%M:%S")
            json_data["validTo"] = (now + relativedelta(days=20)).strftime("%Y/%m/%d %H:%M:%S")
            json_data["brand"] = random.choice(setter_getter.get_brand_id_lst())
            json_data["maxRedeem"] = 1000000
            json_data["redeemCap"] = 100000
            json_data["categories"] = str(setter_getter.get_category_id())
            json_data['userGroup'] = "42"
            json_data["pushType"] = "1"
            try:
                if json_data['skuConditionQuantity']:
                    json_data['skuConditionQuantity'] = '1'
                if json_data['skuConditionActualPrice']:
                    json_data['skuConditionActualPrice'] = '5'
                if json_data['skuConditionSellingPrice']:
                    json_data['skuConditionActualPrice'] = '10'
                if json_data['skuCondition']:
                    json_data['skuCondition'] = str(setter_getter.get_sku_id())
            except KeyError:
                continue
        constants['api_data_multipart1'] = json_data
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(constants['api_data_multipart1'])
    elif(
            data == "data_add_coupon_push_merchant_type_flat_discount_on_sku" and
            file == "file_add_coupon_push_merchant_type_flat_discount_on_sku") or \
            (
                    data == "data_add_coupon_push_merchant_type_Free_SKUs_on_Bill" and
                    file == "file_add_coupon_push_merchant_type_Free_SKUs_on_Bill") or \
            (
                    data == "data_add_coupon_push_merchant_type_Free_SKUs_on_SKUs" and
                    file == "file_add_coupon_push_brand_type_Free_SKUs_on_SKUs") or \
            (
                    data == "data_add_coupon_push_merchant_type_flat_discount" and
                    file == "file_add_coupon_push_merchant_type_flat_discount") or \
            (
                    data == "data_add_coupon_push_merchant_type_Percentage_discount_on_SKU" and
                    file == "file_add_coupon_push_merchant_type_Percentage_discount_on_SKU") or \
            (
                    data == "data_add_coupon_push_merchant_type_Percentage_discount_on_Bill" and
                    file == "file_add_coupon_push_merchant_type_Percentage_discount_on_Bill"):

        json_data = apiBodyDict.get(data)
        constants['coupon_details'] = helpercodes.assig_coupon_details()
        constants['api_file_multipart'] = constants['coupon_details']['image']
        for _ in json_data.items():
            json_data['couponStartTime'] = datetime.utcnow().isoformat()
            json_data['couponEndTime'] = datetime.utcnow().isoformat()
            json_data['title'] = constants['coupon_details']['name']
            json_data['merchant'] = setter_getter.get_merchant_list()[0]
            json_data['source'] = random.choice(['discover', 'prime'])
            json_data['startDate'] = now.strftime("%Y/%m/%d")
            json_data['endDate'] = (now + relativedelta(days=10)).strftime("%Y/%m/%d")
            json_data["validFrom"] = now.strftime("%Y/%m/%d %H:%M:%S")
            json_data["validTo"] = (now + relativedelta(days=20)).strftime("%Y/%m/%d %H:%M:%S")
            json_data["maxRedeem"] = 1000000
            json_data["redeemCap"] = 100000
            json_data["categories"] = str(setter_getter.get_category_id())
            json_data["pushType"] = "1"
            try:
                if json_data['skuConditionQuantity']:
                    json_data['skuConditionQuantity'] = '1'
                if json_data['skuConditionActualPrice']:
                    json_data['skuConditionActualPrice'] = '5'
                if json_data['skuConditionSellingPrice']:
                    json_data['skuConditionActualPrice'] = '10'
                if json_data['skuCondition']:
                    json_data['skuCondition'] = str(setter_getter.get_sku_id())
            except KeyError:
                continue
        constants['api_data_multipart1'] = json_data
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(constants['api_data_multipart1'])
    elif data == 'create_merchant_group':
        setter_getter.set_random_char_generator(14)
        merchant_list = args[0]
        json_data = apiBodyDict.get(data)
        json_data['idList'] = merchant_list
        json_data['name'] = 'merchant_group'+setter_getter.get_random_char_generator()
        json_data['userGroup'] = "42"
        constants['api_data_multipart1'] = json.dumps(json_data)
        setter_getter.set_file(None)
        setter_getter.set_data(constants['api_data_multipart1'])
    elif data == 'create_segment':
        setter_getter.set_random_char_generator(5)
        json_data = apiBodyDict.get(data)
        json_data['name'] = 'Test'+setter_getter.get_random_char_generator()
        json_data['customSegmentId'] = setter_getter.get_random_char_generator()
        json_data['userGroup'] = "42"
        setter_getter.set_file(None)
        setter_getter.set_data(json.dumps(json_data))
    elif data == 'data_create_coupon_group' and file == 'file_create_coupon_group':
        json_data = apiBodyDict.get(data)
        setter_getter.set_random_char_generator(5)
        constants['api_file_multipart'] = constants['coupon_details']['image']
        json_data['name'] = 'Test'+setter_getter.get_random_char_generator()
        try:
            json_data['idList[]'] = (setter_getter.get_coupon_list())[0:4]
        except KeyError:
            pass
        constants['api_data_multipart1'] = json_data
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(constants['api_data_multipart1'])
    elif data == 'data_create_brand' and file == 'file_create_brand':
        json_data = apiBodyDict.get(data)
        constants['api_file_multipart'] = constants['coupon_details']['image']
        json_data['name'] = "{}_{}".format(constants['coupon_details']['brand_name'], setter_getter.get_external_id())
        json_data['externalId'] = setter_getter.get_external_id()
        # json_data['externalId'] = str(random.randint(100891, 100900))
        json_data['userGroup'] = "42"
        constants['api_data_multipart1'] = json_data
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(constants['api_data_multipart1'])
    elif data == '' and file == '':
        pass

    else:
        constants['api_data_multipart1'] = apiBodyDict.get(data)
        constants['api_file_multipart'] = apiBodyDict.get(file)
        setter_getter.set_file(constants['api_file_multipart'])
        setter_getter.set_data(constants['api_data_multipart1'])


def change_mandatory_parameters(parameters):
    data1 = (json.loads(constants['api_Body']))
    if parameters in data1['promotions'][0]:
        data1['promotions'][0].pop(parameters, None)
    constants['api_Body'] = json.dumps(data1, ensure_ascii=False)
    setter_getter.set_body(constants['api_Body'])
