# 用户服务的查询及修改信息接口压测脚本
import random

from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class User_Service(TaskSet):

    def on_start(self):
        print('开始压测p平台用户服务。。。')

    @task(7)
    def user_service(self):
        '''用户信息查询接口'''
        header = {
            "tenantId": 2021110300001,
        }
        userId = [19146961, 19146960, 19138943, 16401971, 16397363, 16396903, 16396265, 16395817, 16395813, 16395811,
                  16395809, 16393279, 16043685, 16041675, 16040793, 16040387, 16040235, 16040233, 16040125, 16038447,
                  16038443, 16038435, 16038433, 16038429, 16038365, 16038071, 16038067, 16037851, 16036669, 16035719,
                  16035545, 15942657, 15567583, 15567556, 15567536, 15567511, 15566256, 10028378, 10028360, 10028358,
                  10028353, 10028351, 10028343, 10028333, 10028332, 10028330, 10028329, 10028327, 10028323, 10028321,
                  10028319, 10028316, 10028311, 10028308, 10028300, 10028299, 10028277, 10027800, 10026149, 10026100,
                  10026095, 10026027, 10025989, 10025925, 10015788, 10015785, 10015770, 10015768, 10015753, 10015750,
                  10015731, 10015345, 10015335, 10015333, 10015314, 10015308, 10014480, 10014468, 10014464, 10014413,
                  10014180, 10014179, 10014156, 10014153, 10014152, 10014151, 10013628, 10012582, 10012335, 10012321,
                  10012242, 10010992, 10010866, 10010226, 10009551, 10009544, 10009534, 10009525, 10009505, 10009135,
                  10007609, 10006818, 10006632, 10006626, 10006622, 10006618, 10006579, 10006534, 10006533, 10006530,
                  10006529, 10006494, 10006417, 10006414, 10006409, 10006397, 10006386, 10006376, 10006375, 10006373,
                  10006372, 10006371, 10006370, 10006368, 10006366, 10006348, 10006341, 10006293, 10005826, 10005825,
                  10005757, 10005701, 10005506, 10005496, 10005455, 10005411, 10005406, 10005392, 10005390, 10005384,
                  10005382, 10005381, 10005379, 10005378, 10005366, 10005362, 10005327, 10005325, 10005321, 10005310,
                  10005292, 10005273, 10005270, 10005260, 10005257, 10005256, 10005252, 10005250, 10005218, 10005198,
                  10004791, 10004786, 10004770, 10004758, 10004757, 10004754, 10004753, 10004749, 10004748, 10004719,
                  10004709, 10004669, 10004615, 10004614, 10004587, 10004571, 10004424, 10004367, 10003616, 10003611,
                  10003610, 10003608, 10003606, 10003605, 10003382, 10003379, 10003331, 10003330, 10003254, 10002474,
                  10002308, 10002161, 10002097, 10002050, 10002045, 10002044, 10001969, 10001879, 10001867, 10001591,
                  10001555, 10001552, 10001550, 10001542, 10001540, 10001535, 10001463, 10001387, 10001351, 10001210,
                  10001206, 10001202, 10001200, 10001185, 10001183, 10001181, 10001169, 10001168, 10001164, 10001161,
                  10001159, 10001138, 10001129, 10001126, 10001117, 10001092, 10001071, 10001066, 10000990, 10000929,
                  10000907, 10000764, 10000763, 10000646, 10000627, 10000598, 10000521, 6507006, 6468098, 6468096,
                  6456782, 6453686, 6453642, 6453582, 6453478, 6453475, 6453367, 6453024, 6450948, 6450935, 6450838,
                  6450826, 6450811, 6450781, 6450311, 6444134, 6443630, 6443623, 6443588, 6443586, 6443583, 6443580,
                  6443572, 6443569, 6443562, 6443322, 6443302, 6443290, 6443224, 6442898, 6442462, 6442327, 6442036,
                  6442019, 6441935, 6441896, 6441651, 6441463, 6441152, 6441085, 6440271, 6440055, 6440018, 6440002,
                  6439954, 6439950, 6439940, 6439928, 6439834, 6439833, 6439777, 6439581, 6439560, 6439514, 6438813,
                  6438643, 6438530, 6438452, 6438398, 6438354, 6438310, 6438290, 6438285, 6438282, 6438281, 6438279,
                  6438275, 6438248, 6438217, 6438213, 6438147, 6438011, 6437729, 6433480, 6431805, 6431795, 6431768,
                  6431759, 6431661, 6431658, 6431657, 6431452, 6431237, 6430920, 6426877, 6426871, 6426710, 6426577,
                  6426435, 6426370, 6426303, 6426272, 6426240, 6426236, 6426164, 6426035, 6425997, 6425634, 6425585,
                  6425577, 6425559, 6425540, 6425506, 6425501, 888888, 404247, 401506, 401338, 88888, 38400, 38399,
                  34845, 28523, 15973, 1023, 917, 916, 915, 892, 877, 844, 824, 657, 332, 327, 326, 307, 287, 256, 249,
                  245, 244, 235, 227, 222, 219, 213, 47, 46, 41, 40, 38, 36, 35, 33, 30, 27, 26, 23, 21, 19, 18, 17, 15,
                  14, 11, 9, 8, 4, 1]
        phoneNumber = [13718415257, 18511708729, 19925378163, 13810954638, 13600000111, 15910952173, 14751790841,
                       13907837307, 13301766238, 13611648116, 13262557670, 13810954638, 18845761552, 18811005339,
                       18511254779, 18383619025, 17521080662, 18090879186, 17633332917, 17621202805, 15021145261,
                       13689285664, 15221143726, 17394082244, 17717059402, 13611987657, 17717059403, 16600000000,
                       15501008293, 18032613663, 18518016199, 13552001339, 18200140020, 13699074211, 13520089824,
                       17610900271, 18896827787, 13017595599, 15201385893, 00000000000, 17707387860, 15755109568,
                       13590161577, 13501762479, 18025133662, 13590476189, 15889964886, 15021575018, 13136597471,
                       17610225668, 15683085270, 18127078675, 17707387860, 18359206293, 13801003680, 15677285945,
                       13396254127, 15846756955, 13601003680, 18518296504, 15810599430, 17090134190, 18612030467,
                       15203500971, 44488888866, 44413173741, 17712645678, 15215070973, 18601011074, 15901167943,
                       18520276544, 44456895832, 44415215070, 44474125809, 15010209830, 17090134190, 13033643031,
                       15578084665, 18210468637, 17090134190, 13810954638, 44441234567, 13221904478, 15560033022,
                       15811853740, 44412345628, 15910820541, 15203500961, 44443573573, 44412355666, 13366254127,
                       15578084665, 44412341234, 13917634889, 44412121212, 18650802640, 44411111111, 13810954638,
                       13810954638, 13810954638, 44412345578, 17770895617, 44499999999, 15578084665, 13667152882,
                       13076925427, 18810458828, 18202606096, 44433333336, 13874904274, 13600519514, 15578084665,
                       44411124458, 18612030467, 13428669065, 44489760543, 13522273857, 15116219579, 18802272582,
                       13422857221, 44412345888, 44494949494, 15062297362, 44412312312, 15010377478, 13221904478,
                       15676313442, 15203500971, 15911152671, 15910820541, 18701586221, 18612030467, 15203500971,
                       15901167943, 18612030467, 44455555555, 13810077987, 44441235186, 44465485764, 44412580369,
                       44412582656, 44471171111, 13045766870, 18612030467, 44488886666, 13814000684, 15910820541,
                       15321392952, 13221904478, 15203500971, 18612030467, 18351812358, 18520837992, 44413246587,
                       44466667777, 44448888888, 44412345890, 44455556666, 44400001111, 13221904478, 44487654321,
                       44436853654, 44484562447, 44444441111, 44420508080, 44442345678, 44489634725, 44423232323,
                       44466666666, 13810077987, 15203500971, 44432586321, 44412356789, 44488888888, 44412345808,
                       13810460931, 15678864914, 13045766870, 44475395125, 44412345678, 44411111111, 44412652586,
                       44422222222, 44400000000, 44444444444, 15013646520, 18603105846, 15910820541, 18519109588,
                       13221904478, 13910961525, 15013646520, 15578993740, 13221820564, 13116677434, 13116657604,
                       13221904478, 13810954638, 14444441444, 13221904478, 18801206516, 13428669065, 18395028490,
                       13145837891, 18651218462, 13810954638, 13396775699, 18810791736, 15249247642, 13774504184,
                       15013646520, 15846488637, 15203500971, 18810223040, 13245538264, 18518437322, 13641069195,
                       13026592725, 13116677434, 15132376105, 15013646520, 15321392952, 18810223040, 13810954638,
                       18611221122, 18801206516, 18612310823, 13701042296, 13467694635, 18610289732, 18651218462,
                       13145837891, 15605083090, 15652828912, 18577503953, 13366254127, 15047992004, 16601156704,
                       17610925657, 16600000000, 17610825657, 13717728604, 18770810813, 17610827673, 16600000008,
                       15931608430, 15120050484, 15210894741, 16600000001, 13221904478, 16600000000, 17625267958,
                       19902020202, 18943870879, 17610900000, 17090134190, 18606379117, 13783580261, 15910200658,
                       17001121111, 13524685789, 13188888889, 15810286655, 15927002067, 15705102295, 13426123762,
                       13581924147, 18080051415, 17600105228, 17871749939, 13260661836, 15996981217, 18600205480,
                       17318632851, 15010238718, 15626539548, 17712341234, 13128804925, 18332537567, 18946751932,
                       18039510833, 18066602218, 18866708737, 13713838798, 15890055363, 17717331642, 18247449586,
                       18157102271, 15139381191, 18617035743, 18668010561, 17792989136, 18587192619, 17301766278,
                       18810102770, 13370146364, 13379409741, 18841412672, 18529167382, 18841412642, 15881159373,
                       13173741806, 17001128896, 13888888888, 13699274542, 15010035497, 17000000000, 18108039227,
                       15558888777, 13016338448, 13311178037, 15554444777, 17700000003, 13552210063, 17700000009,
                       17700000008, 17700000007, 17700000005, 17700000002, 17700000001, 17700000000, 15911156271,
                       13811063928, 15911159671, 15677245142, 13466660053, 15810200657, 15611786897, 18722183573,
                       17610900271, 18101052224, 18612030467, 13466660053, 13700000001, 17665289981, 13717728604,
                       17600452488, 13600000000, 13700000000, 13222222222, 18201058992, 15801582238, 18610909732,
                       18601202860, 13810460232, 18612317605, 18610909732, 15911152671, 18610909732, 15810764361,
                       13611146591, 18601011074, 15999999999, 18734452513, 13810460235, 18601382900, 18500547076,
                       15203577805, 13033985872, 18382313787, 13810575165, 17000000500, 17000000333, 17000000001,
                       17000000004, 17000000003, 15500000000, 13033643031, 18611384951, 15901033661, 13810460931,
                       15700000002, 13200000000, 15810599430, 18518296504, 15203500971, 15010209830, 18601952859,
                       15501008293, 13611146591, 13999999999, 15677285945, 13366254127, 13426456889, 15700000001,
                       18710256026, 13221904478, 15676313442, 13240055263, 18601011074, 13396775699, 15910820541,
                       13810954638, 18513832094, 17090134190, 15911152671, 13810077987, 13810460232, 15901167943,
                       13693694273]
        res = self.client.get(
            'user/v1/query?userId=' + str(random.choice(userId)) + '&phoneNumber=' + str(random.choice(phoneNumber)),
            headers=header, name='用户信息查询接口（有数据）')
        if res.status_code != 200:
            print('Response error message is: ', res.text)
        else:
            pass

    @task(1)
    def user_service_nodata(self):
        '''用户信息查询接口'''
        header = {
            "tenantId": 2021110300001,
        }
        res = self.client.get(
            'user/v1/query?userId=0&phoneNumber=0', headers=header, name='用户信息查询接口（无数据）')
        if res.status_code != 200:
            print('Response error message is: ', res.text)
        else:
            pass

    # @task(1)
    # def userInfo_edit(self):
    #     '''用户信息修改接口'''
    #     header = {
    #         "tenantId": 2021110300001,
    #     }
    #     sex = ["MALE", "FEMALE"]
    #     res = self.client.post(
    #         'user/v1/change', headers=header, json={"sex": random.choice(sex), "userId": 19162756},
    #         name='用户信息修改接口（改性别）')
    #     print(res.text)
        # if res.status_code != 200:
        #     print('Response error message is: ', res.text)
        # else:
        #     pass


class Web_User_Service(FastHttpUser):
    tasks = [User_Service]
    min_wait = 1000
    max_wait = 3000
    host = "http://user.intra.sit.etcp.net:80/"
