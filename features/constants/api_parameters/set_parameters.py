# Created By Rahul Ranjan on 26/08/2018.

from features.constants import helpercodes, setter_getter
from features.constants.apiBody import parameters
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
constants = {}


def modify_and_set_parameters(params):
    if params == 'GetAllCouponIDFromPromoID':
        data = parameters.get(params)
        data["endTs"] = now.strftime("%Y-%m-%d")
        data["startTs"] = (now - relativedelta(days=5)).strftime("%Y-%m-%d")
        constants['setParameters'] = data
    else:
        constants['setParameters'] = parameters.get(params)
    setter_getter.set_parameter(constants['setParameters'])
