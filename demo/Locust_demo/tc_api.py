from zbtest.bdd.consts.servers import TC
from zbtest.bdd.features.rpc.core import InvokeDubboApi
from zbtest.bdd.features.web.tc_http import tc_try_auto_bad_debt_by_cut_time, tc_gen_bad_debt_by_cut_time


def tc_open_trade_payment(env='qa', **kwargs):
    conn = InvokeDubboApi(*TC[env.lower()])
    rs = conn.invoke_dubbo_api('cn.etcp.tradecenter.facade.OpenTradeFacade', 'payment', kwargs)
    return rs


def tc_query_order_polling(env, kwargs):
    conn = InvokeDubboApi(*TC[env.lower()])
    rs = conn.invoke_dubbo_api('cn.etcp.tradecenter.facade.QueryOrderFacade', 'queryOrderPolling', kwargs)
    return rs


def tc_parking_trade_parking_trade(env, kwargs):
    conn = InvokeDubboApi(*TC[env.lower()])
    rs = conn.invoke_dubbo_api('cn.etcp.tradecenter.facade.ParkingTradeFacade', 'parkingTrade', kwargs)
    return rs


def tc_manual_trade_offline_trade(env, kwargs):
    conn = InvokeDubboApi(*TC[env.lower()])
    rs = conn.invoke_dubbo_api('cn.etcp.tradecenter.facade.ManualTradeFacade', 'offlineTrade', kwargs)
    return rs


def tc_manual_trade_trade(env, kwargs):
    conn = InvokeDubboApi(*TC[env.lower()])
    rs = conn.invoke_dubbo_api('cn.etcp.tradecenter.facade.ManualTradeFacade', 'trade', kwargs)
    return rs


def tc_manual_trade_public_id_trade(env, kwargs):
    conn = InvokeDubboApi(*TC[env.lower()])
    rs = conn.invoke_dubbo_api('cn.etcp.tradecenter.facade.ManualTradeFacade', 'publicIdTrade', kwargs)
    return rs


def tc_query_order_query_order(*args, env='qa'):
    conn = InvokeDubboApi(*TC[env.lower()])
    rs = conn.invoke_dubbo_api('cn.etcp.tradecenter.facade.QueryOrderFacade', 'queryOrder',
                               *args)
    return rs


def tc_parking_trade_parking_trade_before_pass(env, kwargs):
    conn = InvokeDubboApi(*TC[env.lower()])
    rs = conn.invoke_dubbo_api('cn.etcp.tradecenter.facade.ParkingTradeFacade', 'parkingTradeBeforePass', kwargs)
    return rs


# 上海公交卡ETC坏账自动补缴
def try_auto_bad_debt_by_cut_time(far_time_in_min, pay_way, action, close_time_in_min=0, env='mock'):
    """
    :param far_time_in_min: 查询订单ontime的最大偏移量，单位为分
    :param pay_way: 查询订单payway
    :param action: 0-重试或产生坏账 1-自动补缴坏账
    :param close_time_in_min: 查询订单ontime的最小偏移量，单位为分
    :param env: 调用环境
    :return: 无实际意义
    """
    func = [tc_gen_bad_debt_by_cut_time, tc_try_auto_bad_debt_by_cut_time][action]
    start_time = int(far_time_in_min) * 1000 * 60
    end_time = int(close_time_in_min) * 1000 * 60
    data = {
        "cutStartTime": start_time,
        "cutEndTime": end_time,
        "payWays": pay_way
    }
    return func(data, env)
