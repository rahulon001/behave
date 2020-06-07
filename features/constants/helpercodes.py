# Created By Rahul Ranjan on 24/06/2018.
import random, os, json, math
from shutil import rmtree
import requests
import pandas as pd
from requests import Session
from features.constants.urls import urlDict
from features.constants.apiBody import couponDetails, merchant_details,sku_data
from features.constants import setter_getter

s = Session()
path3 = os.path.dirname(__file__)


def edit_header(header):
    if 'x-anti-forgery' in header:
        api_request_header_anti_forge = header
        api_request_header_anti_forge['x-anti-forgery'] = setter_getter.get_anti_forge()
        return api_request_header_anti_forge

###################

def raise_request(http_request_type):
    print("----url----", setter_getter.get_url())
    print("----body----", setter_getter.get_body())
    print("----header----", setter_getter.get_header())
    if 'GET' == http_request_type:
        response_full = requests.get(url=setter_getter.get_url(),
                                     headers=setter_getter.get_header(),
                                     params=setter_getter.get_parameter(), verify=False)
        setter_getter.set_response(response_full)
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()

    elif 'POST' == http_request_type:
        response_full = requests.post(url=setter_getter.get_url(),
                                      data=setter_getter.get_body(),
                                      headers=setter_getter.get_header(), verify=False)
        setter_getter.set_response(response_full)
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()

    elif 'PUT' == http_request_type:
        response_full = requests.put(url=setter_getter.get_url(),
                                     data=setter_getter.get_body(),
                                     headers=setter_getter.get_header(), verify=False)
        setter_getter.set_response(response_full)
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()

    elif 'DELETE' == http_request_type:
        response_full = requests.delete(url=setter_getter.get_url(), verify=False)
        setter_getter.set_response(response_full)
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()


def raise_request_with_parameters(http_request_type):
    if 'GET' == http_request_type:
        print("----url----",setter_getter.get_url())
        print("----parameter----",setter_getter.get_parameter())
        print("----header----",setter_getter.get_header())
        response_full = requests.get(url=setter_getter.get_url(),
                                     headers=setter_getter.get_header(),
                                     params=setter_getter.get_parameter(), verify=False)
        setter_getter.set_response(response_full)
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()

    elif 'POST' == http_request_type:
        print("----url----", setter_getter.get_url())
        print("----parameter----", setter_getter.get_parameter())
        print("----header----", setter_getter.get_header())
        print("----body----", setter_getter.get_body())
        response_full = requests.post(url=setter_getter.get_url(),
                                      data=setter_getter.get_body(),
                                      headers=setter_getter.get_header(),
                                      params=setter_getter.get_parameter(), verify=False)
        setter_getter.set_response(response_full)
        print("----response text----", response_full.text)
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()


def raise_request_multipart_secure(http_request_type):
    global s
    if "POST" == http_request_type:
        # print("----url----",setter_getter.get_url())
        # print("----file----",setter_getter.get_file())
        # print("----data----",setter_getter.get_data())
        # print("----header----",setter_getter.get_header())
        response_full = s.post(url=setter_getter.get_url(),
                               files=setter_getter.get_file(),
                               data=setter_getter.get_data(),
                               headers=setter_getter.get_header(), verify=False)
        setter_getter.set_response(response_full)
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()
    elif "GET" == http_request_type:
        print("----url----",setter_getter.get_url())
        print("----header----",setter_getter.get_header())
        response_full = s.get(url=setter_getter.get_url(),
                              params=setter_getter.get_parameter(),
                              headers=setter_getter.get_header(), verify=False)
        setter_getter.set_response(response_full)
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()
    elif "DELETE" == http_request_type:
        print("----url----",setter_getter.get_url())
        print("----header----",setter_getter.get_header())
        response_full = s.delete(url=setter_getter.get_url(),
                                 headers=setter_getter.get_header(), verify=False)
        setter_getter.set_response(response_full)
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()


def raise_request_multipart_file_data(http_request_type):
    if "POST" == http_request_type:
        response_full = requests.post(url=setter_getter.get_url(),
                                      files=setter_getter.get_file(),
                                      data=setter_getter.get_data(), verify=False)
        setter_getter.set_response(response_full)
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()


# login to CMS


def login_to_cms():
    global s
    url = urlDict.get('cmsLogin')
    payload = "username=admin1&password=f01d71e6e38fc7d8afec846de6c512ce310dd1bf6ab1003c9a2a93729795295d"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }
    resp = s.post(url, data=payload, headers=headers, verify=False)
    anti_forgery = str(resp.headers['x-anti-forgery'])
    setter_getter.set_anti_forge(anti_forgery)
    print('login to CMS', resp)


def access_token():
    url = urlDict.get('MyjioAccessToken')
    payload = {'username': "9945240311", 'password': "jiomoney@2", 'grant_type': "password"}
    headers = {
        'Authorization': "Basic bDd4eDNlODg3NDAzYjVlZDQwZTc4Y2E4ZWRlZjY1Yzg3NTg3OmM2NDU1NjhhOTI3NzQ1YTY5NmUwZTUyZTU4N"
                         "zFiZTgz",
        'Content-Type': "application/x-www-form-urlencoded"
    }
    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    print('access_token_response', response)
    return json.loads(response.text)["access_token"]


def verify_response(expected_response_code):
    actual_response_code = setter_getter.get_response().status_code
    if str(actual_response_code) != str(expected_response_code):
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)


def validate_responcee():
    if None in setter_getter.get_response():
        raise('Null response received')


def create_couponcode_redeem_file(lst):
    res = []
    data = lst[0]
    for j in range(10):
        res.append(random.randint(1982, 81882882))
    raw_data1 = {'PromotionId': data, 'CouponCode': res}
    raw_data2 = {'CouponCode': res}
    df1 = pd.DataFrame(raw_data1, columns=['PromotionId', 'CouponCode'])
    df2 = pd.DataFrame(raw_data2, columns=['CouponCode'])
    # print("Z"*100,filename)
    df1.to_csv(path3 + '/files/couponcode.csv', index=False)
    # print("G"*100, df1)
    df2.to_csv(path3 + '/files/redemptions.csv', index=False)


def create_list_with_random_element(num):
    lst = []
    for i in range(num):
        setter_getter.set_random_char_generator(5)
        lst.append(setter_getter.get_random_char_generator())
    return lst

def assig_coupon_details():
    foo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    return couponDetails.get(random.choice(foo))


def assig_merchant_details():
    foo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    return merchant_details.get(random.choice(foo))


def assign_sku_detail():
    foo = ['A', 'B', 'C', 'D', 'E', 'F']
    return sku_data.get(random.choice(foo))


def assign_coupon_body():
    choice = {
        'A': ('data_add_coupon_pull_merchant_type_flat_discount_on_sku',
              'file_add_coupon_pull_merchant_type_flat_discount_on_sku',
              'add_coupon_pull_merchant_type'),        # add_coupon_pull_merchant_type_flat_discount_on_sku_or_type
        'B': ('data_add_coupon_pull_merchant_type_Free_SKUs_on_Bill',
              'file_add_coupon_pull_merchant_type_Free_SKUs_on_Bill',
              'add_coupon_pull_merchant_type'),        # add_coupon_pull_merchant_type_Free_SKUs_on_Bill__or_type
        'C': ('data_add_coupon_pull_merchant_type_Free_SKUs_on_SKUs',
              'file_add_coupon_pull_merchant_type_Free_SKUs_on_SKUs',
              'add_coupon_pull_merchant_type'),        # add_coupon_pull_merchant_type_Free_SKUs_on_SKUs__or_type
        'D': ('data_add_coupon_pull_merchant_type_flat_discount',
              'file_add_coupon_pull_merchant_type_flat_discount',
              'add_coupon_pull_merchant_type'),        # add_coupon_pull_merchant_type_flat_discount
        'E': ('data_add_coupon_pull_merchant_type_Percentage_discount_on_SKU',
              'file_add_coupon_pull_merchant_type_Percentage_discount_on_SKU',
              'add_coupon_pull_merchant_type'),  # add_coupon_pull_merchant_type_Percentage_discount_on_SKU_or_type
        'F': ('data_add_coupon_pull_merchant_type_Percentage_discount_on_Bill',
              'file_add_coupon_pull_merchant_type_Percentage_discount_on_Bill',
              'add_coupon_pull_merchant_type'),  # add_coupon_pull_merchant_type_Percentage_discount_on_Bill_or_type
        # 'M': ('', '', ''),          # add_coupon_pull_merchant_type_flat_discount_on_sku_and_type
        # 'N': ('', '', ''),          # add_coupon_pull_merchant_type_Free_SKUs_on_Bill__and_type
        # 'O': ('', '', ''),          # add_coupon_pull_merchant_type_Free_SKUs_on_SKUs__and_type
        # 'P': ('', '', ''),          # add_coupon_pull_merchant_type_Percentage_discount_on_SKU__and_type
        # 'Q': ('', '', ''),          # add_coupon_pull_merchant_type_Percentage_discount_on_Bill__and_type

        'G': ('data_add_coupon_pull_brand_type_flat_discount_on_sku',
              'file_add_coupon_pull_brand_type_flat_discount_on_sku',
              'add_coupon_pull_brand_type'),          # add_coupon_pull_brand_type_flat_discount_on_sku__or_type
        'H': ('data_add_coupon_pull_brand_type_Free_SKUs_on_Bill',
              'file_add_coupon_pull_brand_type_Free_SKUs_on_Bill',
              'add_coupon_pull_brand_type'),          # add_coupon_pull_brand_type_Free_SKUs_on_Bill__or_type
        'I': ('data_add_coupon_pull_brand_type_Free_SKUs_on_SKUs',
              'file_add_coupon_pull_brand_type_Free_SKUs_on_SKUs',
              'add_coupon_pull_brand_type'),          # add_coupon_pull_brand_type_Free_SKUs_on_SKUs__or_type
        'J': ('data_add_coupon_pull_brand_type_flat_discount',
              'file_add_coupon_pull_brand_type_flat_discount',
              'add_coupon_pull_brand_type'),          # add_coupon_pull_brand_type_flat_discount
        'K': ('data_add_coupon_pull_brand_type_Percentage_discount_on_SKU',
              'file_add_coupon_pull_brand_type_Percentage_discount_on_SKU',
              'add_coupon_pull_brand_type'),    # add_coupon_pull_brand_type_Percentage_discount_on_SKU__or_type
        'L': ('data_add_coupon_pull_brand_type_Percentage_discount_on_Bill',
              'file_add_coupon_pull_brand_type_Percentage_discount_on_Bill',
              'add_coupon_pull_brand_type'),    # add_coupon_pull_brand_type_Percentage_discount_on_Bill__or_type
        # 'R': ('', '', ''),          # add_coupon_pull_brand_type_flat_discount_on_sku__and_type
        # 'S': ('', '', ''),          # add_coupon_pull_brand_type_Free_SKUs_on_Bill__and_type
        # 'T': ('', '', ''),          # add_coupon_pull_brand_type_Free_SKUs_on_SKUs__and_type
        # 'W': ('', '', ''),          # add_coupon_pull_brand_type_Percentage_discount_on_SKU__and_type
        # 'X': ('', '', ''),          # add_coupon_pull_brand_type_Percentage_discount_on_Bill__and_type
    }
    # foo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    foo = ['G', 'I', 'K']        # brand type coupons
    # foo = ['A', 'C', 'E']          # merchant type coupon
    select_coupon = random.choice(foo)
    (data, file, url) = choice.get(select_coupon)
    return data, file, url


#This function will make branches_num per city
def coordinate_distributions(city,lat, long, merchant_id, branches_num=1, radius_1=10):
    print("city>>>>>",(city))
    print("merchant_id>>>>>", (merchant_id))
    print("branch_num>>>>>", (branches_num))
    print("given_radius>>>>>", (radius_1))
    a_list, b_list, c_list, d_list, e_list, f_list, g_list, h_list, i_list = [], [], [], [], [], [], [], [], []
    radius = random.randint(1, int(radius_1))                     # m - reasonably accurate for distances < 100km
    branches = random.randint(1, int(branches_num))               # varying number of branches in different cities
    center_lat = float(lat)                                       # latitude of circle center, decimal degrees
    center_lon = float(long)                                      # Longitude of circle center, decimal degrees
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
        a_list.append(merchant_id)                              # merchant
        b_list.append(zone)                                     # zone
        c_list.append(city)                                     # state
        d_list.append(city)                                     # city
        e_list.append(city)                                     # address
        f_list.append(pin)                                      # pin
        g_list.append(format(float(lat), ".8f"))   # latitude
        h_list.append(format(float(lon), ".8f"))   # latitude
        i_list.append(pin)                                      # shop_number
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
    setter_getter.set_merchant_branch_data(raw_data)
    df = pd.DataFrame(raw_data)
    setter_getter.set_random_char_generator(14)
    rand = setter_getter.get_random_char_generator()
    with open('{}/files/address_info/address_info_{}.csv'.format(path3, rand), 'w+') as address_info:
        df.to_csv(address_info, index=False)
    del a_list, b_list, c_list, d_list, e_list, f_list, g_list, h_list, df


def create_address_info():
    new_path = "{}/files/address_info".format(path3)
    if not os.path.exists(new_path):
        os.makedirs(new_path)


def delete_address_info_csv_file():
    rand = setter_getter.get_random_char_generator()
    file_path = "{}/files/address_info/address_info_{}.csv".format(path3,rand)
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("The file does not exist")


def delete_address_info():
    new_path = "{}/files/address_info".format(path3)
    if os.path.exists(new_path):
        rmtree(new_path)


merchant_list = []

def merchant_lst(merchant_id):
    merchant_list.append(merchant_id)
    return merchant_list


def delete_masID():
    new_path = "{}/files/barcode_data_updated".format(path3)
    if os.path.exists(new_path):
        rmtree(new_path)


def random_sku_(ran_1):
    if ran_1 == 6:
        random_sku = "{0}|{1}|{2}|{3}|{4}|{5}".format(random.randint(800000, 10000000),
                                                      random.randint(800000, 10000000),
                                                      random.randint(800000, 10000000),
                                                      random.randint(800000, 10000000),
                                                      random.randint(800000, 10000000),
                                                      random.randint(800000, 10000000))
        return random_sku
    elif ran_1 == 5:
        random_sku = "{0}|{1}|{2}|{3}|{4}".format(random.randint(800000, 10000000),
                                                  random.randint(800000, 10000000),
                                                  random.randint(800000, 10000000),
                                                  random.randint(800000, 10000000),
                                                  random.randint(800000, 10000000))
        return random_sku
    elif ran_1 == 4:
        random_sku = "{0}|{1}|{2}|{3}".format(random.randint(800000, 10000000),
                                              random.randint(800000, 10000000),
                                              random.randint(800000, 10000000),
                                              random.randint(800000, 10000000))
        return random_sku
    elif ran_1 == 3:
        random_sku = "{0}|{1}|{2}".format(random.randint(800000, 10000000),
                                          random.randint(800000, 10000000),
                                          random.randint(800000, 10000000))
        return random_sku
    elif ran_1 == 2:
        random_sku = "{0}|{1}".format(random.randint(800000, 10000000),
                                      random.randint(800000, 10000000))
        return random_sku


# if __name__ == "__main__":
# coordinate_distributions(merchant_id=23926, branches_num=1, radius_1=50)
