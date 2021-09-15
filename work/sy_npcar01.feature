# Created by Todd at 2021/9/15
Feature: 新能源车费率通用
  # 新能源车费率通用方案测试用例（默认车型，跨区，长租车，特殊车型，新能源车类型）
    Scenario: 01默认车型费率，只有默认车型，符合纯电小车
        Given 停车场："sy测试车场1"，获取停车场信息
        And   岗亭："岗亭1"，获取岗亭信息
        And   车场"sy测试车场1"设置"重庆新能源"车型为"新能源车"默认车型
        And   车场"sy测试车场1"设置"低型1cpd"车型为"普通车"默认车型

        When  车辆"京Q6QD18"在这个时间"2021-09-15 18:14:00"通过"岗亭1"岗亭下的"区域1"区域的"入口1"入道口
        And   车辆"京Q6QD18"在这个时间"<any>"通过"<any>"岗亭下的"<any>"区域的"<any>"入道口
        Then  车辆进出场状态及费用
                |car_num|msg|应收金额|
                |京Q6QD18|欢迎光临|0.01||

    Scenario: 02默认车型费率，只有默认车型，符合纯电小车第二次
        Given 停车场："sy测试车场1"，获取停车场信息
        And   岗亭："岗亭1"，获取岗亭信息
        When  车辆"京Q6QD18"在这个时间"2021-09-15 18:14:00"通过"岗亭1"岗亭下的"区域1"区域的"入口1"入道口
        And   出口岗亭选择"<any>"车型


    Scenario: 03默认车型费率，只有默认车型，符合纯电大车第一次
        Given 停车场："sy测试车场1"，获取停车场信息
        And   岗亭："岗亭1"，获取岗亭信息
        When  车辆"京Q6QD18"在这个时间"2021-09-15 18:14:00"通过"岗亭1"岗亭下的"区域1"区域的"入口1"入道口
        And   出口岗亭选择"<any>"车型


    Scenario: 04默认车型费率，只有默认车型，符合纯电大车第二次
        Given 停车场："sy测试车场1"，获取停车场信息
        And   岗亭："岗亭1"，获取岗亭信息
        When  车辆"京Q6QD18"在这个时间"2021-09-15 18:14:00"通过"岗亭1"岗亭下的"区域1"区域的"入口1"入道口
        And   出口岗亭选择"<any>"车型

    Scenario: 05默认车型费率，只有默认车型，符合混动小车第一次
        Given 停车场："sy测试车场1"，获取停车场信息
        And   岗亭："岗亭1"，获取岗亭信息
        When  车辆"京Q6QD18"在这个时间"2021-09-15 18:14:00"通过"岗亭1"岗亭下的"区域1"区域的"入口1"入道口
        And   出口岗亭选择"<any>"车型


    Scenario: 06默认车型费率，只有默认车型，符合混动小车第二次
        Given 停车场："sy测试车场1"，获取停车场信息
        And   岗亭："岗亭1"，获取岗亭信息
        When  车辆"京Q6QD18"在这个时间"2021-09-15 18:14:00"通过"岗亭1"岗亭下的"区域1"区域的"入口1"入道口
        And   出口岗亭选择"<any>"车型


    Scenario: 07默认车型费率，只有默认车型，符合混动大车第一次
        Given 停车场："sy测试车场1"，获取停车场信息
        And   岗亭："岗亭1"，获取岗亭信息
        When  车辆"京Q6QD18"在这个时间"2021-09-15 18:14:00"通过"岗亭1"岗亭下的"区域1"区域的"入口1"入道口
        And   出口岗亭选择"<any>"车型


    Scenario: 08默认车型费率，只有默认车型，符合混动大车第二次
        Given 停车场："sy测试车场1"，获取停车场信息
        And   岗亭："岗亭1"，获取岗亭信息
        When  车辆"京Q6QD18"在这个时间"2021-09-15 18:14:00"通过"岗亭1"岗亭下的"区域1"区域的"入口1"入道口
        And   出口岗亭选择"<any>"车型


    Scenario: 09默认车型费率，只有默认车型，普通车第一次
        Given 停车场："sy测试车场1"，获取停车场信息
        And   岗亭："岗亭1"，获取岗亭信息
        When  车辆"京Q6QD18"在这个时间"2021-09-15 18:14:00"通过"岗亭1"岗亭下的"区域1"区域的"入口1"入道口
        And   出口岗亭选择"<any>"车型


    Scenario: 10默认车型费率，只有默认车型，普通车第二次
        Given 停车场："sy测试车场1"，获取停车场信息
        And   岗亭："岗亭1"，获取岗亭信息
        When  车辆"京Q6QD18"在这个时间"2021-09-15 18:14:00"通过"岗亭1"岗亭下的"区域1"区域的"入口1"入道口
        And   出口岗亭选择"<any>"车型