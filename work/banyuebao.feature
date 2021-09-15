Feature: 新版半月保  (业务支撑平台)_62

	Scenario: test01-01不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB001"在这个时间"2017-09-01 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB001"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB001|欢迎光临|0.0|
				|京BYB001|一路顺利|0.0|
				
	Scenario: test01-02不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯非工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB001"在这个时间"2017-09-02 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB001"在这个时间"2017-09-02 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB001|欢迎光临|0.0|
				|京BYB001|一路顺利|0.0|
				
	Scenario: test01-03不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB001"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB001"在这个时间"2017-09-02 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB001|欢迎光临|0.0|
				|京BYB001|一路顺利|0.0|
				
	Scenario: test01-04不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从非工作日跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB001"在这个时间"2017-09-03 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB001"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB001|欢迎光临|0.0|
				|京BYB001|一路顺利|0.0|
				
	Scenario: test01-05不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB001"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB001"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB001|欢迎光临|0.0|
				|京BYB001|一路顺利|0.0|
				
	Scenario: test01-06不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从非工作日跨到工作日再跨到非工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB001"在这个时间"2017-09-03 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB001"在这个时间"2017-09-09 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB001|欢迎光临|0.0|
				|京BYB001|一路顺利|0.0|
				
	Scenario: test02-05不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB002"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB002"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB002|欢迎光临|0.0|
				|京BYB002|一路顺利|0.0|
				
	Scenario: test02-06不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从非工作日跨到工作日再跨到非工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB002"在这个时间"2017-09-03 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB002"在这个时间"2017-09-09 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB002|欢迎光临|0.0|
				|京BYB002|一路顺利|0.0|
				
	Scenario: test03-05不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB003"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB003"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB003|欢迎光临|0.0|
				|京BYB003|待支付|84.0|
				
	Scenario: test03-06不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从非工作日跨到工作日再跨到非工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB003"在这个时间"2017-09-03 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB003"在这个时间"2017-09-09 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB003|欢迎光临|0.0|
				|京BYB003|待支付|138.0|
				
	Scenario: test04-05不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB004"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB004"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB004|欢迎光临|0.0|
				|京BYB004|待支付|204.0|
				
	Scenario: test04-06不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从非工作日跨到工作日再跨到非工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB004"在这个时间"2017-09-03 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB004"在这个时间"2017-09-09 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB004|欢迎光临|0.0|
				|京BYB004|待支付|402.0|

	Scenario: test05-01不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB005"在这个时间"2017-09-01 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB005"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|欢迎光临|0.0|
				|京BYB005|待支付|2.0|
				
	Scenario: test05-02不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯非工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB005"在这个时间"2017-09-02 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB005"在这个时间"2017-09-02 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|欢迎光临|0.0|
				|京BYB005|待支付|3.0|				

	Scenario: test05-05不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB005"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB005"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|欢迎光临|0.0|
				|京BYB005|待支付|48.0|
				
	Scenario: test06-01不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB006"在这个时间"2017-09-01 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB006"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB006|欢迎光临|0.0|
				|京BYB006|待支付|4.0|
				
	Scenario: test06-02不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯非工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB006"在这个时间"2017-09-02 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB006"在这个时间"2017-09-02 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB006|欢迎光临|0.0|
				|京BYB006|待支付|5.0|				

	Scenario: test06-05不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB006"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB006"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB006|欢迎光临|0.0|
				|京BYB006|待支付|84.0|
				
	Scenario: test07-01不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB007"在这个时间"2017-09-01 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB007"在这个时间"2017-09-01 22:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB007|欢迎光临|0.0|
				|京BYB007|待支付|2.0|
				
	Scenario: test07-02不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯非工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB007"在这个时间"2017-09-02 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB007"在这个时间"2017-09-02 22:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB007|欢迎光临|0.0|
				|京BYB007|待支付|3.0|				

	Scenario: test07-05不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB007"在这个时间"2017-09-01 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB007"在这个时间"2017-09-04 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB007|欢迎光临|0.0|
				|京BYB007|待支付|40.0|
				
	Scenario: test08-01不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB008"在这个时间"2017-09-01 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB008"在这个时间"2017-09-01 22:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB008|欢迎光临|0.0|
				|京BYB008|待支付|6.0|
				
	Scenario: test08-02不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯非工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB008"在这个时间"2017-09-02 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB008"在这个时间"2017-09-02 22:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB008|欢迎光临|0.0|
				|京BYB008|待支付|7.0|				

	Scenario: test08-05不区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB008"在这个时间"2017-09-01 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB008"在这个时间"2017-09-04 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB008|欢迎光临|0.0|
				|京BYB008|待支付|96.0|
				
	Scenario: test41-01区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB041"在这个时间"2017-09-01 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB041"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB041|欢迎光临|0.0|
				|京BYB041|待支付|2.0|
				
	Scenario: test41-02区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯非工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB041"在这个时间"2017-09-02 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB041"在这个时间"2017-09-02 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB041|欢迎光临|0.0|
				|京BYB041|一路顺利|0.0|

	Scenario: test41-05区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB041"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB041"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB041|欢迎光临|0.0|
				|京BYB041|待支付|12.0|
				
	Scenario: test48-01区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB048"在这个时间"2017-09-01 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB048"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB048|欢迎光临|0.0|
				|京BYB048|待支付|4.0|
				
	Scenario: test48-02区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯非工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB048"在这个时间"2017-09-02 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB048"在这个时间"2017-09-02 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB048|欢迎光临|0.0|
				|京BYB048|待支付|14.0|

	Scenario: test48-05区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB048"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB048"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB048|欢迎光临|0.0|
				|京BYB048|待支付|192.0|
				
	Scenario: test53-01区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB053"在这个时间"2017-09-01 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB053"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB053|欢迎光临|0.0|
				|京BYB053|待支付|2.0|
				
	Scenario: test53-02区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯非工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB053"在这个时间"2017-09-02 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB053"在这个时间"2017-09-02 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB053|欢迎光临|0.0|
				|京BYB053|待支付|3.0|

	Scenario: test53-05区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB053"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB053"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB053|欢迎光临|0.0|
				|京BYB053|待支付|48.0|
				
	Scenario: test56-01区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB056"在这个时间"2017-09-01 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB056"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB056|欢迎光临|0.0|
				|京BYB056|待支付|6.0|
				
	Scenario: test56-02区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，纯非工作日进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB056"在这个时间"2017-09-02 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB056"在这个时间"2017-09-02 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB056|欢迎光临|0.0|
				|京BYB056|待支付|5.0|

	Scenario: test56-05区分工作日和非工作日，有效时段为全长租，临停费率为默认车型，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB056"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB056"在这个时间"2017-09-04 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB056|欢迎光临|0.0|
				|京BYB056|待支付|96.0|
				
	Scenario: test68-05区分工作日和非工作日，工作日有效时段从大到小，非工作日有效时段从小到大，从工作日跨到非工作日再跨到工作日============
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB068"在这个时间"2017-09-01 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB068"在这个时间"2017-09-04 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB068|欢迎光临|0.0|
				|京BYB068|待支付|72.0|
				
	Scenario: test72-05区分工作日和非工作日，工作日有效时段从大到小，非工作日有效时段从大到小，从工作日跨到非工作日再跨到工作日===============
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB072"在这个时间"2017-09-01 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB072"在这个时间"2017-09-04 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB072|欢迎光临|0.0|
				|京BYB072|待支付|92.0|
				
	Scenario: test73-05区分工作日和非工作日，有效时段跨有效期结束时间点
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB007"在这个时间"2017-09-15 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB007"在这个时间"2017-09-16 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB007|欢迎光临|0.0|
				|京BYB007|待支付|11.0|
				
	Scenario: test74-02区分工作日和非工作日，有效期前进场，有效期内出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB005"在这个时间"2017-08-31 22:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB005"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|临时进入|0.0|
				|京BYB005|待支付|10.0|
				
	Scenario: test74-04区分工作日和非工作日，有效期内进场，有效期后出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB005"在这个时间"2017-09-14 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB005"在这个时间"2017-09-16 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|欢迎光临|0.0|
				|京BYB005|待支付|33.0|
				
	Scenario: test74-06不区分工作日和非工作日，进出场跨整个有效期
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB005"在这个时间"2017-08-31 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB005"在这个时间"2017-09-16 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|临时进入|0.0|
				|京BYB005|待支付|237.0|
				
	Scenario: test75-01不区分工作日和非工作日，有效期内倒车
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB005"在这个时间"2017-09-01 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        When  车辆"京BYB505"在这个时间"2017-09-01 08:10:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB005"在这个时间"2017-09-01 09:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        And   车辆"京BYB505"在这个时间"2017-09-01 09:30:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|欢迎光临|0.0|
				|京BYB505|临时进入|0.0|
				|京BYB005|一路顺利|0.0|
				|京BYB505|待支付|1.0|
				
	Scenario: test75-02不区分工作日和非工作日，过期后倒车
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB005"在这个时间"2017-09-18 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        When  车辆"京BYB505"在这个时间"2017-09-18 08:10:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB005"在这个时间"2017-09-18 09:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        And   车辆"京BYB505"在这个时间"2017-09-18 09:30:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|临时进入|0.0|
				|京BYB505|临时进入|0.0|
				|京BYB005|待支付|1.0|
				|京BYB505|待支付|2.0|
				
	Scenario: test076一车多位，出口计费
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB076"在这个时间"2017-09-08 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB076"在这个时间"2017-09-16 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB076|欢迎光临|0.0|
				|京BYB076|待支付|123.0|
				
	Scenario: test77跨区  (A区 >  B区  >  A区) 
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB005"在这个时间"2017-09-01 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        When  车辆"京BYB005"在这个时间"2017-09-01 09:00:00"通过"半月保岗亭"岗亭下的"B区"区域的"B区次入"入道口
        When  车辆"京BYB005"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区次入"入道口
        And   车辆"京BYB005"在这个时间"2017-09-01 11:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口        
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|欢迎光临|0.0|
				|京BYB005|临时进入|0.0|
				|京BYB005|欢迎光临|0.0|
				|京BYB005|待支付|1.0|
				
	Scenario: test77-02跨区  ( B区 ) 
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB005"在这个时间"2017-09-01 08:00:00"通过"半月保岗亭"岗亭下的"B区"区域的"B区主入"入道口
        And   车辆"京BYB005"在这个时间"2017-09-01 11:00:00"通过"半月保岗亭"岗亭下的"B区"区域的"B区主出"出道口        
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|临时进入|0.0|
				|京BYB005|待支付|3.0|
				
	Scenario: test78全车场半月保  (A区 >  B区  >  A区) 
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB078"在这个时间"2017-09-01 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        When  车辆"京BYB078"在这个时间"2017-09-01 09:00:00"通过"半月保岗亭"岗亭下的"B区"区域的"B区次入"入道口
        When  车辆"京BYB078"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区次入"入道口
        And   车辆"京BYB078"在这个时间"2017-09-01 11:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口        
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB078|欢迎光临|0.0|
				|京BYB078|临时进入|0.0|
				|京BYB078|欢迎光临|0.0|
				|京BYB078|待支付|1.0|
				
	Scenario: test079法定节假日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB079"在这个时间"2017-09-19 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB079"在这个时间"2017-09-21 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB079|临时进入|0.0|
				|京BYB079|待支付|52.0|
				
	Scenario: test101区分工作日和非工作日，工作日有效时段从大到小，非工作日有效时段从小到大，从工作日跨到非工作日再跨到工作日
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB101"在这个时间"2017-09-01 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB101"在这个时间"2017-09-04 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB101|欢迎光临|0.0|
				|京BYB101|待支付|108.0|
				
	Scenario: test102区分工作日和非工作日，从工作日跨到非工作日再跨到工作日，无非工作日费率走工作日费率
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB102"在这个时间"2017-09-01 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB102"在这个时间"2017-09-04 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB102|欢迎光临|0.0|
				|京BYB102|待支付|132.0|
				
			

	Scenario: test103-01进出场结合半月保达到限额
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB103"在这个时间"2017-09-01 06:00:00"通过"半月保岗亭"岗亭下的"C区"区域的"C区主入"入道口
        And   车辆"京BYB103"在这个时间"2017-09-01 17:00:00"通过"半月保岗亭"岗亭下的"C区"区域的"C区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB103|欢迎光临|0.0|
				|京BYB103|待支付|6.0|
				
	Scenario: test103-02跨区达到限额再返回（A区 > C区 > A区）
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB102"在这个时间"2017-09-04 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB102"在这个时间"2017-09-04 22:00:00"通过"半月保岗亭"岗亭下的"C区"区域的"C区次入"入道口
        And   车辆"京BYB102"在这个时间"2017-09-05 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区次入"入道口
        And   车辆"京BYB102"在这个时间"2017-09-05 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB102|欢迎光临|0.0|
				|京BYB102|临时进入|0.0|
				|京BYB102|欢迎光临|0.0|
				|京BYB102|待支付|47.0|

	Scenario: test103-03跨区未达限额再返回（A区 > C区 > A区）
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB102"在这个时间"2017-09-04 18:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
        And   车辆"京BYB102"在这个时间"2017-09-04 22:00:00"通过"半月保岗亭"岗亭下的"C区"区域的"C区次入"入道口
        And   车辆"京BYB102"在这个时间"2017-09-05 02:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区次入"入道口
        And   车辆"京BYB102"在这个时间"2017-09-05 12:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB102|欢迎光临|0.0|
				|京BYB102|临时进入|0.0|
				|京BYB102|欢迎光临|0.0|
				|京BYB102|待支付|22.0|
				
	Scenario: test104-01半月卡长租，有效期内进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB104"在这个时间"2017-09-04 18:00:00"通过"半月保岗亭"岗亭下的"C区"区域的"C区主入"入道口
        And   车辆"京BYB104"在这个时间"2017-09-05 12:00:00"通过"半月保岗亭"岗亭下的"C区"区域的"C区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB104|欢迎光临|0.0|
				|京BYB104|一路顺利|0.0|
				
	Scenario: test104-02半月卡长租，有效期内入场，有效期外出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB104"在这个时间"2017-09-16 18:00:00"通过"半月保岗亭"岗亭下的"C区"区域的"C区主入"入道口
        And   车辆"京BYB104"在这个时间"2017-09-17 05:00:00"通过"半月保岗亭"岗亭下的"C区"区域的"C区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB104|欢迎光临|0.0|
				|京BYB104|待支付|5.0|
				
	Scenario: test104-03半月卡长租，有效期外进出场
        Given 停车场："神州一号车场"，获取停车场信息
        And   岗亭："半月保岗亭"，获取岗亭信息
        When  车辆"京BYB104"在这个时间"2017-09-18 18:00:00"通过"半月保岗亭"岗亭下的"C区"区域的"C区主入"入道口
        And   车辆"京BYB104"在这个时间"2017-09-19 10:00:00"通过"半月保岗亭"岗亭下的"C区"区域的"C区主出"出道口
        Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB104|临时进入|0.0|
				|京BYB104|待支付|5.0|
				
	Scenario: test105有效时段跨有效期结束时间点
		Given 停车场："神州一号车场"，获取停车场信息
		And   岗亭："半月保岗亭"，获取岗亭信息
		When  车辆"京BYB068"在这个时间"2017-09-15 19:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
		And   车辆"京BYB068"在这个时间"2017-09-16 01:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
		Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB068|欢迎光临|0.0|
				|京BYB068|待支付|4.5|
				
	Scenario: test106-01半月保车辆一位多车时跨有效时段--有到无
		Given 停车场："神州一号车场"，获取停车场信息
		And   岗亭："半月保岗亭"，获取岗亭信息
		When  车辆"京BYB005"在这个时间"2017-09-01 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
		And   车辆"京BYB505"在这个时间"2017-09-01 11:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
		And   车辆"京BYB005"在这个时间"2017-09-01 20:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
		And   车辆"京BYB505"在这个时间"2017-09-01 21:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
		Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|欢迎光临|0.0|
				|京BYB505|临时进入|0.0|
				|京BYB005|一路顺利|0.0|
				|京BYB505|待支付|10.0|
				
	Scenario: test106-02半月保车辆一位多车时跨有效时段--无到有
		Given 停车场："神州一号车场"，获取停车场信息
		And   岗亭："半月保岗亭"，获取岗亭信息
		When  车辆"京BYB005"在这个时间"2017-09-01 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
		And   车辆"京BYB505"在这个时间"2017-09-01 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
		And   车辆"京BYB005"在这个时间"2017-09-01 10:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
		And   车辆"京BYB505"在这个时间"2017-09-01 12:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
		Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|欢迎光临|0.0|
				|京BYB505|临时进入|0.0|
				|京BYB005|待支付|2.0|
				|京BYB505|待支付|2.0|
				
	Scenario: test106-03半月保车辆一位多车时跨有效时段--有无有
		Given 停车场："神州一号车场"，获取停车场信息
		And   岗亭："半月保岗亭"，获取岗亭信息
		When  车辆"京BYB005"在这个时间"2017-09-01 08:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
		And   车辆"京BYB505"在这个时间"2017-09-01 19:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
		And   车辆"京BYB005"在这个时间"2017-09-01 21:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
		And   车辆"京BYB505"在这个时间"2017-09-02 09:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
		Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|欢迎光临|0.0|
				|京BYB505|临时进入|0.0|
				|京BYB005|待支付|1.0|
				|京BYB505|待支付|17.0|
				
	Scenario: test106-04半月保车辆一位多车时跨有效时段--无有无
		Given 停车场："神州一号车场"，获取停车场信息
		And   岗亭："半月保岗亭"，获取岗亭信息
		When  车辆"京BYB005"在这个时间"2017-09-01 06:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口       
		And   车辆"京BYB505"在这个时间"2017-09-01 09:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主入"入道口
		And   车辆"京BYB005"在这个时间"2017-09-01 21:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
		And   车辆"京BYB505"在这个时间"2017-09-01 22:00:00"通过"半月保岗亭"岗亭下的"A区"区域的"A区主出"出道口
		Then  车辆进出场状态及费用
				|car_num|msg|应收金额|
				|京BYB005|欢迎光临|0.0|
				|京BYB505|临时进入|0.0|
				|京BYB005|待支付|3.0|
				|京BYB505|待支付|13.0|
				
				