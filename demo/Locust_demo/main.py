import asyncio
import math
import pathlib
import time
from datetime import datetime

import requests
from icecream import ic

from zbtest.bdd.consts import dt_fmt
# from zbtest.bdd.features.city_drivers import verify_upload_infinitely
from zbtest.bdd.features.billing_drivers import (
    verify_cached_rsp_by_park_and_source, verify_rsp_by_park_and_source,
    is_one_clearing,
)
# from zbtest.bdd.features.city_drivers import verify_upload_infinitely
from zbtest.bdd.features.common_net_drivers import settle_member_bind_info
from zbtest.bdd.features.etcc_drivers import create_etcc_order
from zbtest.bdd.features.open_drivers import (
    city_shanghai_query_cost, city_shanghai_pay_notify,
    city_shanghai_download_pay_results, merchant_withhold_notify, verify_zhengzhou_upload_infinitely,
    openapi_user_sign_in_single, openapi_order_pay, openapi_bind_car, open_api_repay_debt, openapi_withhold_sign,
)
from zbtest.bdd.features.qianfan.parking_business import parking_biz_etcp_mock_car_out
from zbtest.bdd.features.qianfan.parking_client import parking_app_order_create, check_parking_app_order_create
from zbtest.bdd.features.qianfan.trade import (
    qf_trade_order_create, order_success, pay_notify,
    check_pay_notify
)
from zbtest.bdd.features.rpc.tc_api import (
    tc_open_trade_payment, tc_parking_trade_parking_trade,
    tc_query_order_query_order,
)
from zbtest.bdd.features.tc_drivers import manual_trade_offline_trade
from zbtest.bdd.features.web.pc_http import (
    pc_enterprise_notify_enterprise_withhold_,
    pc_enterprise_notify_enterprise_refund_,
)
from zbtest.bdd.structure.parking import get_latest_shard_c_parking_record, get_mqtt_login
from zbtest.bdd.structure.payment import get_user_id_of_car
from zbtest.bdd.structure.qianfan.parking import query_parking_info
from zbtest.bdd.structure.qianfan.scripts import go_flow
from zbtest.utils.mqtt import start_listening_to_mqtt
from zbtest.utils.partials import compact_json
from zbtest.utils.sql2txt import parse_sql, wrt
from zbtest.utils.time_shift import split_dt


def main1(park_id, pay_date):
    return city_shanghai_download_pay_results(park_id, pay_date)


def main(park_id, plate_id, notify=False, vehicle_type=1, pay_status=1, pay_type=2, env='qa'):
    cost = city_shanghai_query_cost(park_id, plate_id, vehicle_type, env=env)['data']
    breakpoint()
    if notify:
        business_id = cost['businessId']
        order_id = cost['orderId']
        due_money = cost['dueMoney']
        return city_shanghai_pay_notify(park_id, business_id, order_id, plate_id, vehicle_type,
                                        due_money, pay_status, pay_type)
    else:
        return cost


def open_trade_payment(plate_number, order_id="SH20201014SJ310110000140000001", is_force=True, is_withhold=False,
                       receivable_fee=0.01, mark='ZZFMYT', on_time=None, pay_time=None, plat_coupon_amount=0.00):
    latest_parking_record = get_latest_shard_c_parking_record(plate_number)
    kwargs = {
        "code": 0, "couponFree": 0.00, "externalDiscount": "0", "externalOrderId": order_id,
        "mark": mark, "onTime": on_time or int(time.mktime(datetime.now().timetuple()) * 1000),
        "orderId": "", "parkCouponId": "", "payTime": pay_time or int(time.mktime(datetime.now().timetuple()) * 1000),
        "receivableFee": receivable_fee, "shangHaiPlatCouponAmt": plat_coupon_amount,
        "synId": latest_parking_record.syn_id, "userId": get_user_id_of_car(plate_number),
        "force": str(is_force).lower(), "withHold": str(is_withhold).lower()
    }
    return tc_open_trade_payment('qa', **kwargs)


def parking_trade_parking_trade(plate_number, order_id="SH20201014SJ310110000140000001",
                                area_id=3161, box_id=10003642, paid_amount=0.01, mark="ZZFMYT",
                                exit_time=None, paid_time=None, parking_id=1003505, receivable_fee=0.01, ):
    latest_parking_record = get_latest_shard_c_parking_record(plate_number)
    kwargs = {
        "actualFee": 0.00, "adminId": 6159, "areaId": area_id, "artificial": 'false',
        "boxPaidArray": [{
            "payFrom": 5,
            "payWay": 71,
            "source": 3,
            "exitMachineSn": 0,
            "transNo": order_id,
            "paidTime": datetime.now().strftime(dt_fmt),
            "paidAmount": paid_amount,
            "mark": mark
        }], "busCardFee": 0,
        "enough": 'true',
        "entranceTime": int(time.mktime(latest_parking_record.entrance_time.timetuple()) * 1000),
        "exemptMoney": 0.0, "exitMachineSn": 0,
        "exitParkingBoxId": box_id,
        "exitTime": exit_time or int(time.mktime(datetime.now().timetuple()) * 1000),
        "fees": 0.01, "paidAmount": 0.0,
        "paidTime": paid_time or int(time.mktime(datetime.now().timetuple()) * 1000),
        "parkCouponCount": 0, "parkCouponFree": 0, "parkingId": parking_id, "payFrom": 0,
        "payWay": 0, "plateColor": 1, "plateNumber": plate_number, "receivableFee": receivable_fee, "source": 3,
        "storageCardFee": 0, "synId": latest_parking_record.syn_id, "withdrawable": 0
    }
    kwargs = {
        "actualFee": 0.00,
        "adminId": 6128,
        "areaId": 3230,
        "artificial": 'false',
        "boxPaidArray": [
            {
                "payFrom": 5,
                "payWay": 68,
                "merchantData": "{\"subMerchantId\":\"999110101020190\",\"parkRecordTime\":\"14秒\",\"vehplateColor\":\"0\",\"vehplateNo\":\"吉BA1Y44\",\"entranceTime\":\"20210929213754\",\"exitTime\":\"20210929213808\",\"laneId\":\"999\",\"exitNo\":\"999\",\"sType\":\"9001\",\"rCode\":\"0000\",\"paySerialNo\":\"907ca46808fd42f9841680db07c80e04\",\"exitOrderNo\":\"907ca46808fd42f9841680db07c80e04\",\"outOrderNo\":\"907ca46808fd42f9841680db07c80e04\",\"transAmount\":2,\"deductAmount\":2,\"chargingType\":\"0\",\"cardChipNo\":\"2021092921380991\",\"transTime\":\"20210929213809\",\"terminalId\":\"211100000001\",\"psamId\":\"2\",\"cardSerialNo\":\"00F9\",\"psamSerialNo\":\"01020331\",\"cardRnd\":\"FFFFFFFF\",\"tac\":\"DA53EC19\",\"cardNetNo\":\"1101\",\"transBeforeBalance\":500000000000,\"balance\":499999999998,\"transType\":\"09\",\"cardType\":\"22\",\"deviceType\":\"0\",\"deviceNo\":\"\",\"originalTransInfo\":\"\",\"remark\":\"成功\",\"payType\":\"2\",\"obuId\":\"1448eeae\",\"vehicleType\":\"1\",\"algorithmType\":\"1\",\"issuerIdentifier\":\"b1b1bea911010001\",\"serialNumber\":\"1101120173278762\",\"transSerialSn\":\"\",\"YeeHawETCCardType\":0}",
                "source": 3,
                "exitMachineSn": 0,
                "transNo": "907ca46808fd42f9841680db07c80e04",
                "paidTime": "2021-09-29 21:38:09",
                "paidAmount": 0.02,
                "mark": "0"
            }
        ],
        "busCardFee": 0,
        "enough": 'true',
        "entranceTime": 1632922674000,
        "exemptMoney": 0.0,
        "exitCarImage": "吉BA1Y44_202109292138089589_out.jpg",
        "exitMachineSn": 0,
        "exitParkingBoxId": 10003770,
        "exitTime": 1632922688000,
        "fees": 0.00,
        "paidAmount": 0.0,
        "paidTime": -62135798400000,
        "parkCouponCount": 0,
        "parkCouponFree": 0,
        "parkingId": 1003591,
        "payFrom": 0,
        "payWay": 0,
        "plateColor": 0,
        "plateNumber": "吉BA1Y44",
        "receivableFee": 0.01,
        "source": 3,
        "storageCardFee": 0,
        "synId": "907CA468-08FD-42F9-8416-80DB07C80E04",
        "withdrawable": 0,
        "extendBizPayInfo": {
            "chargeCar": {
                "chargeFee": 0.01,
                "seizeFee": 0.01
            }
        }
    }
    return tc_parking_trade_parking_trade('qa', kwargs)


def sh_etc_parking_trade(data, pay_way=0, fees=0.0):
    entrance_time = split_dt(data['entrance_time'])
    paid_time = split_dt(data['trans_time'])
    exit_time = split_dt(data['exit_time'])
    plate_number = data['card_sn']
    latest_parking_record = get_latest_shard_c_parking_record(plate_number)
    paid_fee = data['receivable_total_amount'] / 100
    parking_id = latest_parking_record.parking_id
    syn_id = latest_parking_record.syn_id
    kwargs = {
        "actualFee": 0.00, "adminId": 6159, "areaId": latest_parking_record.area_id, "artificial": 'false',
        "boxPaidArray": [{
            "payFrom": 5,
            "payWay": pay_way,
            "source": 3,
            "exitMachineSn": 0,
            "transNo": data['trans_order_no'],
            "paidTime": '{year}-{month:0>2}-{day:0>2} {hour:0>2}:{minute:0>2}:{second:0>2}'.format(**paid_time),
            "paidAmount": paid_fee,
            "merchantData": compact_json(data)
        }], "busCardFee": 0,
        "enough": 'true',
        "entranceTime": int(time.mktime(datetime(**entrance_time).timetuple()) * 1000),
        "exemptMoney": 0.0, "exitMachineSn": 0,
        "exitParkingBoxId": latest_parking_record.exit_parking_box_id,
        "exitTime": int(time.mktime(datetime(**exit_time).timetuple()) * 1000),
        "fees": fees, "paidAmount": paid_fee,
        "paidTime": int(time.mktime(datetime(**paid_time).timetuple()) * 1000),
        "parkCouponCount": 0, "parkCouponFree": 0, "parkingId": parking_id, "payFrom": 5,
        "payWay": pay_way, "plateColor": 1, "plateNumber": plate_number,
        "receivableFee": paid_fee + fees, "source": 3,
        "storageCardFee": 0, "synId": syn_id, "withdrawable": 0
    }
    return tc_parking_trade_parking_trade('mock', kwargs)


def sut_etc_parking_trade_with_coupons(data, coupons, park_coupon_count=0,
                                       park_coupon_fee=0, park_coupon_id=None,
                                       fees=0.0, first='e'):
    pay_way = 68
    entrance_time = split_dt(data['entranceTime'])
    paid_time = split_dt(data['transTime'])
    exit_time = split_dt(data['exitTime'])
    plate_number = data['vehplateNo']
    paid_fee = data['transAmount'] / 100
    latest_parking_record = get_latest_shard_c_parking_record(plate_number)
    parking_id = latest_parking_record.parking_id
    syn_id = latest_parking_record.syn_id
    e = [{
        "payFrom": 5,
        "payWay": pay_way,
        "source": 3,
        "exitMachineSn": 0,
        "transNo": data['trans_order_no'],
        "paidTime": '{year}-{month:0>2}-{day:0>2} {hour:0>2}:{minute:0>2}:{second:0>2}'.format(**paid_time),
        "paidAmount": paid_fee,
        "merchantData": compact_json(data)
    }]
    c = [{
        "payFrom": 5,
        "payWay": coupon['coupon_pay_way'],
        "source": 3,
        "exitMachineSn": 0,
        "state": coupon['coupon_state'],
        "transNo": coupon['coupon_data']['code'],
        "paidTime": '{year}-{month:0>2}-{day:0>2} {hour:0>2}:{minute:0>2}:{second:0>2}'.format(**paid_time),
        "paidAmount": coupon['coupon_fee'],
        "merchantData": compact_json({
            "storeId": coupon['coupon_data']['storeId'],
            "orderNo": coupon['coupon_data']['orderNo'],
            "couponNo": coupon['coupon_data']['no'],
            "couponCode": coupon['coupon_data']['code'],
            "couponTitle": coupon['coupon_data']['title'],
            "recordSynId": syn_id,
            "categoryValue": coupon['coupon_data']['categoryValue']
        })
    } for coupon in coupons]
    kwargs = {
        "actualFee": 0.00, "adminId": 6159, "areaId": latest_parking_record.area_id, "artificial": 'false',
        "boxPaidArray": (e + c) if first == 'e' else (c + e), "busCardFee": 0,
        "enough": 'true',
        "entranceTime": int(time.mktime(datetime(**entrance_time).timetuple()) * 1000),
        "exemptMoney": 0.0, "exitMachineSn": 0,
        "exitParkingBoxId": latest_parking_record.exit_parking_box_id,
        "exitTime": int(time.mktime(datetime(**exit_time).timetuple()) * 1000),
        "fees": fees, "paidAmount": paid_fee,
        "paidTime": int(time.mktime(datetime(**paid_time).timetuple()) * 1000),
        "parkCouponCount": park_coupon_count, "parkCouponFree": park_coupon_fee,
        "parkingId": parking_id, "payFrom": 5,
        "payWay": pay_way, "plateColor": 1, "plateNumber": plate_number,
        "receivableFee": paid_fee + fees + coupons[-1]['coupon_fee'], "source": 3,
        "storageCardFee": 0, "synId": syn_id, "withdrawable": 0
    }
    if park_coupon_count == 1:
        kwargs["parkCouponId"] = park_coupon_id
    return tc_parking_trade_parking_trade('qa', kwargs)


def sd_etc_parking_trade_with_coupons(data, coupons, pay_way=0, fees=0.0, first='e'):
    entrance_time = split_dt(data['entrance_time'])
    paid_time = split_dt(data['trans_time'])
    exit_time = split_dt(data['exit_time'])
    plate_number = data['card_sn']
    latest_parking_record = get_latest_shard_c_parking_record(plate_number)
    paid_fee = data['receivable_total_amount'] / 100
    parking_id = latest_parking_record.parking_id
    syn_id = latest_parking_record.syn_id
    e = [{
        "payFrom": 5,
        "payWay": pay_way,
        "source": 3,
        "exitMachineSn": 0,
        "transNo": data['trans_order_no'],
        "paidTime": '{year}-{month:0>2}-{day:0>2} {hour:0>2}:{minute:0>2}:{second:0>2}'.format(**paid_time),
        "paidAmount": paid_fee,
        "merchantData": compact_json(data)
    }]
    c = [{
        "payFrom": 5,
        "payWay": coupon['coupon_pay_way'],
        "source": 3,
        "exitMachineSn": 0,
        "state": coupon['coupon_state'],
        "transNo": coupon['coupon_data']['code'],
        "paidTime": '{year}-{month:0>2}-{day:0>2} {hour:0>2}:{minute:0>2}:{second:0>2}'.format(**paid_time),
        "paidAmount": coupon['coupon_fee'],
        "merchantData": compact_json({
            "storeId": coupon['coupon_data']['storeId'],
            "orderNo": coupon['coupon_data']['orderNo'],
            "couponNo": coupon['coupon_data']['no'],
            "couponCode": coupon['coupon_data']['code'],
            "couponTitle": coupon['coupon_data']['title'],
            "recordSynId": syn_id,
            "categoryValue": coupon['coupon_data']['categoryValue']
        })
    } for coupon in coupons]
    kwargs = {
        "actualFee": 0.00, "adminId": 6159, "areaId": latest_parking_record.area_id, "artificial": 'false',
        "boxPaidArray": (e + c) if first == 'e' else (c + e), "busCardFee": 0,
        "enough": 'true',
        "entranceTime": int(time.mktime(datetime(**entrance_time).timetuple()) * 1000),
        "exemptMoney": 0.0, "exitMachineSn": 0,
        "exitParkingBoxId": latest_parking_record.exit_parking_box_id,
        "exitTime": int(time.mktime(datetime(**exit_time).timetuple()) * 1000),
        "fees": fees, "paidAmount": paid_fee,
        "paidTime": int(time.mktime(datetime(**paid_time).timetuple()) * 1000),
        "parkCouponCount": 0, "parkCouponFree": 0, "parkingId": parking_id, "payFrom": 5,
        "payWay": pay_way, "plateColor": 1, "plateNumber": plate_number,
        "receivableFee": paid_fee + fees + coupons[-1]['coupon_fee'], "source": 3,
        "storageCardFee": 0, "synId": syn_id, "withdrawable": 0
    }
    return tc_parking_trade_parking_trade('qa', kwargs)


def query_order(syn_id, pay_ways, env="grey"):
    return tc_query_order_query_order(syn_id, pay_ways, env=env)


def pay_wx_notify():
    url = 'http://newpay.qa.etcp.cn/service/paymentnotify/notifywx4appid'
    data = '''<xml><appid><![CDATA[wx1346a39b74f847e5]]></appid>
    <attach><![CDATA[009d8217-eaaa-4f91-99eb-8191a2b0729e[2021-03-25 11:03:35]#*#{"pn":"BA1Y46","aid":"wx192b7d2e8dcbefd0"}#*#]]></attach>
    <bank_type><![CDATA[OTHERS]]></bank_type>
    <cash_fee><![CDATA[1]]></cash_fee>
    <fee_type><![CDATA[CNY]]></fee_type>
    <is_subscribe><![CDATA[N]]></is_subscribe>
    <mch_id><![CDATA[1510599141]]></mch_id>
    <nonce_str><![CDATA[1103351122]]></nonce_str>
    <openid><![CDATA[owF2-0f9kmcybeN82_WiK7wVrC7M]]></openid>
    <out_trade_no><![CDATA[p1616641415312001011001402414962]]></out_trade_no>
    <result_code><![CDATA[SUCCESS]]></result_code>
    <return_code><![CDATA[SUCCESS]]></return_code>
    <sign><![CDATA[]]></sign>
    <sub_appid><![CDATA[wx192b7d2e8dcbefd0]]></sub_appid>
    <sub_is_subscribe><![CDATA[N]]></sub_is_subscribe>
    <sub_mch_id><![CDATA[1510770601]]></sub_mch_id>
    <sub_openid><![CDATA[oO-wd0bCWOL8er-u68xfGfxdloNM]]></sub_openid>
    <time_end><![CDATA[20210325110401]]></time_end>
    <total_fee>1</total_fee>
    <trade_type><![CDATA[JSAPI]]></trade_type>
    <transaction_id><![CDATA[4200000988202103253001350183]]></transaction_id>
    </xml>'''
    r = requests.post(url, data=data, headers={"Content-Type": "text/plain"})
    ic(r.text)


def payment_push_to_cs():
    i = 0
    limits = 200
    while i < 150:
        s = time.time()
        msg = {
            "businessData": "{\"CouponMessage\":[],\"WuKcarInfo\":{\"Limits\":%s,\"Mark\":\"\",\"Payway\":0,\"Plate_number\":\"吉BA1Y46\",\"prepay\":0}}" % limits,
            "businessId": "7833f346-b345-4011-8002-20b0dc4802a2", "businessType": "WuKongToParking",
            "methodName": "VerifyWuKuser_TCP", "parkId": "1824", "pushTime": 1616998692549,
            "resTopic": "parking.etcp.user.res", "version": 1
        }
        url = 'http://msgcenter.etcp.cn/msgcenter/message/1.2.0/sendMsgToCS'
        rsp = requests.post(url, data=msg)
        e = time.time()
        ic(f'{e - s}s elapsed')
        ic(f'limits: {limits}')
        ic(rsp.text)
        i += 1
        limits += 1


def batch_1_clear_checking():
    parks = """8424
8382""".splitlines()
    for park_id in parks:
        park_id = int(park_id.strip())
        if is_one_clearing(park_id, 'prod'):
            print(park_id)


async def a(i):
    for x in range(10):
        with open('result.txt', 'a') as fp:
            ic(f'{x}_{i}_{time.time()}')
            fp.write(f'{x}_{i}_{time.time()}\n')
        await asyncio.sleep(2)


async def main2():
    tasks = [asyncio.create_task(a(i)) for i in range(35)]
    [await task for task in tasks]


def div(i):
    rate = 0.006
    return round((i * rate) * 100) / 100


if __name__ == '__main__':
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    # parking_app_order_create()
    plate_number = '黑A3RP06'
    # plate_number = '沪AAAAAA'
    mobile = 15210894741
    park_id = 1003591
    # go_flow('o.txt')
    # ic(create_etcc_order('吉BA1Y44', status=1))
    # park_id = 'cn31010500040'
    # park_id = 5113
    # print(main(park_id, plate_number, notify=False, env='prod'))
    openapi_user_sign_in_single(mobile, 'ETCP')
    # openapi_bind_car(mobile, plate_number, 'ETCP')
    # ic(openapi_order_pay(mobile, plate_number, 5, syn_id='ed15b5d8-f1a7-4f6b-bb20-74e663d60144'))
    # ic(open_api_repay_debt(mobile, 2))
    # openapi_bind_car(mobile, plate_number, 'ETCP')
    # for pay_type in range(1, 6):
    #     ic(openapi_order_pay(mobile, plate_number, pay_type, syn_id='02e99da5-7def-4e3b-8e8e-b4229c5ae79c'))
    #     breakpoint()
    # ic(settle_member_bind_info(1003865, '5538000000036016'))
    # asyncio.run(main2())
    # wrt(parse_sql(pathlib.Path(r'C:\Users\ETCP-001\Desktop\PUB_PAY_BANKA-平安二清银行信息.sql').as_posix()))
    # from multiprocessing import Pool
    #
    # with Pool(processes=10) as p:
    #     r = [p.apply_async(a, (i,)) for i in range(15)]
    #     for _ in r:
    #         _.get()
    # order, pay_order = qf_trade_order_create('15210894741', plate_number, 10000, order_type='park')
    # ic(order)
    # ic(pay_order)
    # order = '1384393410016247808'
    # r = query_parking_info(id=10005087)
    # r0 = r[0]
    # ic(r0.bcd)
    # pay_order = '3384349338533769216'
    # ic(order_success(order))
    # rsp = parking_app_order_create(plate_number, mobile='15210894741')
    # order = rsp['data']['orderNo']
    # ic(bool(check_parking_app_order_create(order)))
    # ic(pay_notify(order))
    # ic(bool(check_pay_notify(order)))
    # ic(parking_biz_etcp_mock_car_out(plate_number))
    # uid, pwd = get_mqtt_login(1003591)
    # start_listening_to_mqtt('10.103.10.26', 50009, uid, pwd, ['parking.1003591', 'parking.10003770'])
    # verify_rsp_by_park_and_source(1003471, 3)
    # d = {
    #     "out_trade_no": "p1614676933699017004001113015128", "pay_time": "2021-03-29 17:05:02", "total_fee": "0.01",
    #     "pay_status": 0, "message": "\u6210\u529f", "trade_no": "816359759260467200"
    # }
    # rd = {
    #     "out_trade_no": "p1584427935014017004001728234773", "out_refund_trade_no": "ref20200317145701137430",
    #     "refund_time": "2021-03-29 18:20:25", "total_fee": "0.01", "pay_status": 0, "message": "\u6210\u529f",
    #     "trade_no": "2021032918202570368729777126", "refund_trade_no": "2021032918202570368729777126"
    # }
    # pc_enterprise_notify_enterprise_withhold_(d, env='prod')
    # pc_enterprise_notify_enterprise_refund_(rd, env='prod')
    # merchant_withhold_notify('p1619104810787017004001568519783', 5.5, '20210422232011032214715f3bd0', app_id='CMB')
    # merchant_refund_notify('p1584427935014017004001728234773', 'ref20200317145701137430', 0.01, app_id='BM')
    # payment_notify_notify_bd_pay()
    # payment_push_to_cs()
    # for pay_way in (54, 143, 43, 18, 46):
    #     manual_trade_offline_trade('吉BA1Y77', offline_fee=0.01, pay_way=pay_way,
    #                                env='qa',
    #                                syn_id='5645133D-5FFC-41B5-BDA9-C413E943CEFD',
    #                                entrance_time='2021-04-21 20:06:23',
    #                                entrance_parking_box_id=10003770,
    #                                parking_id=1003591,
    #                                area_id=3230)
    #     breakpoint()
    # for pay_way in (54, 143, 43, 18, 46):
    #     manual_trade_offline_trade('吉BA1Y77', offline_fee=0.01, pay_way=pay_way,
    #                                env='prod',
    #                                syn_id='cfafc537-a4c1-49e7-9b6d-714928b1059c',
    #                                entrance_time='2021-04-22 22:32:10',
    #                                entrance_parking_box_id=17027,
    #                                parking_id=1824,
    #                                area_id=2378)
    #     breakpoint()
    # ic(openapi_bind_car(15210894741, '吉BA1Y77', 'CNBU'))
    # ic(merchant_withhold_user_status('15210894741', app_id='CNBU'))
    openapi_withhold_sign(mobile, '1')
    # openapi_withhold_status(15210894741, '1')
    # d = {
    #     "subMerchantId": "999110113020001", "parkRecordTime": "3分54秒", "vehplateColor": "1", "vehplateNo": "青QQQMM5",
    #     "entranceTime": "20210318145021", "exitTime": "20210318145436", "laneId": "999", "exitNo": "999",
    #     "sType": "9001", "rCode": "0000", "paySerialNo": "6faca6ed552048bdabcc28cc6f854982",
    #     "exitOrderNo": "6faca6ed552048bdabcc28cc6f854982", "outOrderNo": "6faca6ed552048bdabcc28cc6f854982",
    #     "transAmount": 399, "deductAmount": 399, "chargingType": "0", "cardChipNo": "1201220000660032",
    #     "transTime": "20210318145436", "terminalId": "211100000001", "psamId": "373737373737", "cardSerialNo": "00F9",
    #     "psamSerialNo": "01020331", "cardRnd": "FFFFFFFF", "tac": "DA53EC19", "cardNetNo": "1101",
    #     "transBeforeBalance": "500000000000", "balance": "499999999601", "transType": "09", "cardType": "22",
    #     "deviceType": "2", "deviceNo": "", "originalTransInfo": "", "remark": "成功", "payType": "2", "obuId": "1448eeae",
    #     "vehicleType": "1", "algorithmType": "1", "issuerIdentifier": "b1b1bea911010001",
    #     "serialNumber": "1101120173278762", "transSerialSn": None
    # }
    # c1 = dict(coupon_data={
    #     "category": 2,
    #     "categoryValue": 0.01,
    #     "code": "213127468900333618",
    #     "no": 193628772,
    #     "orderNo": "5D164944F2664E398C3A96D2D699101E",
    #     "storeId": 100000204,
    #     "subtitle": "停车劵7",
    #     "title": "ETCP测试停车劵-0.01"
    # }, coupon_pay_way=75, coupon_fee=0.01, coupon_state=1)
    # sut_etc_parking_trade_with_coupons(d, [c1], fees=0.0, first='e')
    # KunMing.verify_park_free()
    # remove_payment_detail('8250A695-1295-435F-B798-6C6B3BBA985F')
    # print(get_billing_conf(app=11, name='parkDirectClearing.cfg.necessary.payWays'))
    # print(sh_etc_err_plate_del(500, '吉BA1Y01'))
    # print(sh_etc_err_plate_add(500, '吉BA1Y01'))
    # verify_ks_park_info()
    # verify_upload_infinitely(1003944)
    # verify_tz_park_free()
    # verify_tz_park_info()
    # tc_query_order_polling('123')
    # print(merchant_cu_activity_pay_record('15210894741', None).text)
    # verify_rsp_by_park_and_source(1003591)
    # verify_rsp_by_park_and_source(1003657)
    # verify_cached_rsp_by_park_and_source(1003591, source=1)
    # print(deserialize(x))
    # op_park_free_push(env='prod')
    # op_park_info_push(env='prod')
    # print(openapi_send_free_coupon(1003591, '吉BA1Y01', ct=3, cv=0.2, mch='MASCSDN'))
    # print(openapi_send_free_coupon(1003591, '吉BA1Y01', ct=3, cv=0.8, mch='SZEYTPT'))
    # print(sz_6001(1003591, '吉BA1Y01', '2020-11-27 12:57:11', '2020-11-27 17:34:21').text)
    # print(sz_6002('eea608aa-b9f2-4533-ad63-f004b425992f', 1003586).text)
    # from binascii import hexlify, unhexlify
    # from zbtest.utils.secrets.crc import crc_ccitt_encrypt
    # o = unhexlify('020019000100015FB38649B0A1000000BBA6414239373330000000007FFFE81400000D00194203')
    # c = crc_ccitt_encrypt(o, 1, 36)
    # print(hexlify(c))
    # verify_sz_park_info()
    # verify_sz_park_free()
    # print(lottery(15210894741).text)
    # go_check_mas_check('2020-11-12')
    # go_check_redis_statistics('BAIYMAS', '2020-11-12', 1003591)
    # print(openapi_zhengzhou_parking_space(1003591))
    # verify_zhengzhou_parking_space(1003591)
    # verify_zhengzhou_manual_trade('吉BA1Y51', syn_id='3afd2c7a-b89f-43b4-b10c-a59348fb3138',
    #                               parking_id='ECI14636', env="grey")
    # verify_zhengzhou_upload_car_out(1003591, '吉BA1Y01')
    # verify_zhengzhou_upload_infinitely(1003591, '吉BA1Y01')
    # openapi_zhengzhou_upload_car_in(1003591, '吉BA1Y01')
    # print(query_order("5d41894e-9a09-4a07-ae98-21f003e5dc8b", [2], "qa"))
    # print(tc_query_order_polling(
    #     'qa',
    #     {
    #         'orderId': 'no161490847905910927254',
    #         'batchNo': 'c7708dbe-7928-4cb9-8cf6-508adcde295b'
    #     }))
    # print(open_trade_payment('藏Y1AB01', f'mock_{now}0001', is_force=True, is_withhold=True, mark='BAIYZZ'))
    # print(parking_trade_parking_trade('藏Y1AB01', f'mock_{now}0001'))
    # print(main1(1003667, '2020-10-13'))
    # print(city_shanghai_pay_notify(1003667, '20201004sj310110000140000031', 'SH20201004sj310110000140000034',
    #                                '吉SB0001', 1, 1, 1, 1))
