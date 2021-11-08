# 插入停车记录
import uuid
import logging
import sys
import time
from datetime import datetime
from locust import task, events, User, HttpUser, TaskSet
from locust.contrib.fasthttp import FastHttpUser

class UserBehavior(TaskSet):
    """Locust任务集，定义每个locust行为"""

    def on_start(self):
        print("根据订单号查询开放平台订单接口测试")

    def get_response(self, response):
        """
        获取返回
        :param response:请求返回对象
        :return:
        """
        start_time = int(time.time())
        if response.status_code == 200:
            events.request_success.fire(
                request_type="recv",
                name=sys._getframe().f_code.co_name,
                response_time=int(time.time() - start_time) * 1000,
                response_length=0
            )
        else:
            events.request_failure.fire(
                request_type="recv",
                name=sys._getframe().f_code.co_name,
                response_time=int(time.time() - start_time) * 1000,
                response_length=0,
                exception=f"Response Code Error! Code:{response.content}"
            )

    # @task(3)
    # def test_parking_insert(self, plate: str, park_id: int, admin_id: int, company_id: int, active_code: str, area_id: int,
    #                 entrance_box_id: int, entrance_road_id: int, entrance_time: datetime = None, syn_id: str = None,
    #                 entrance_color: int = 0, computer_info='CD592074787964ABE95355AEC2A1C0', version: str = "3.6.5.0"):


class WebUser(FastHttpUser):
# class WebUser(HttpUser):   # 用requsts方法 rps可以很高，但失败事务也很高，用FastHttpUser失败事务很低但rps没有超过30，头疼
    """性能测试配置，换算配置"""
    # task_set = UserBehavior # Testcase类,1.0的旧语法，已经废弃
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
    # host = "https://baidu.com"

def insert_car_record(plate: str, park_id: int, admin_id: int, company_id: int, active_code: str, area_id: int,
                    entrance_box_id: int, entrance_road_id: int, entrance_time: datetime = None, syn_id: str = None,
                    entrance_color: int = 0, computer_info='CD592074787964ABE95355AEC2A1C0', version: str = "3.6.5.0"):
    now = datetime.now()
    syn_id = syn_id or str(uuid.uuid4())
    args_value = {
        "t_PakingRecord": [
            {
                "R_PlateNumber": plate,
                "Id": 3424,
                "TempID": "",
                "Entrance_time": common_dt_str(entrance_time or now),
                "Entrance_CarImage": f"{plate}_{full_dt_str(entrance_time or now)[:18]}_in.jpg",
                "Entrance_parking_box_id": entrance_box_id,
                "Exit_time": "1970-01-01 00:00:00",
                "Exit_CarImage": None,
                "Exit_parking_box_id": None,
                "receivable_Fee": None,
                "actual_Fee": None,
                "Online_Fee": "0.0",
                "Admin_id": admin_id,
                "Ontime": common_dt_str(now),
                "Update_time": common_dt_str(now),
                "ParkingID": park_id,
                "Area_id": area_id,
                "GroupID": syn_id,
                "IsFixed": None,
                "State": None,
                "CarOwnerParkingFixedLocationId": None,
                "Exit_Road": None,
                "Entrance_Road": entrance_road_id,
                "SynID": syn_id,
                "Status": 0,
                "FreeTime": 0,
                "Entrance_CarImageBelieve": 99,
                "Exit_CarImageBelieve": 0,
                "Remarks": None,
                "Entrance_CarPlateColor": entrance_color,
                "Exit_CarPlateColor": 0,
                "OperateUserid": 0,
                "IsFinish": 0,
                "Brand": "",
                "CharacterCode": "\"3.000000 5.000000 219.000000 130.000000 153.000000 18.000000 129.000000 "
                                 "77.000000 327.000000 803.000000 0.999803 0.000116 0.000031 0.000019 0.000019 "
                                 "0.000002 0.000001 0.000001 0.000001 0.000001\"",
                "MotorType": 1,
                "MotorTypeDetail": 0
            }
        ],
        "t_PakingSecondRecord": None,
        "t_CarOwner": None,
        "Cardcarpakingsequenc": None,
        "Paperplate": None
    }
    args = {
        "ClinetIdentity": {
            "ComputerInfo": computer_info,
            "ActiveCode": active_code,
            "CompanyId": company_id,
            "ParkingId": park_id,
            "ParkingBoxId": entrance_box_id,
            "InnerIP": None,
            "Version": version
        },
        "ReqMothedName": "TempUploadPayOrder",
        "ArgsValue": compact_json(args_value),
        "RequestId": None,
        "MSN": None
    }
    data = {
        'parkId': park_id,
        'mothedName': 'TempUploadPayOrder',
        'tArgs': compact_json(args)
    }
    logger.info(f'临停入场参数: {data}')

logger = logging.getLogger()
