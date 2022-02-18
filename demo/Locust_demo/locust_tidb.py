# locust压测Tidb数据库

import pymysql
from locust import task, TaskSet, User
from locust.contrib.fasthttp import FastHttpUser


class TidbTaskSet(User):

    # def run_sql(self):
    #     self.connect = pymysql.connect(
    #         host='tidb.uat.etcp.net', port=5000, user='parking_dev', password='fTg1DIUKb81#tP3#', db='parking')
    #     cursor = self.connect.cursor()
    #     sql = "SELECT id, plate_number, entrance_time, exit_time, receivable_fee, remarks FROM parking_record WHERE plate_number = '渝B52V96';"
    #     cursor.execute(sql)
    #     res = cursor.fetchall()
    #     self.user_list = []
    #     for i in res:
    #         self.user_list.append(i[0])
    #     print(self.user_list)
    #     cursor.close()
    #     self.connect.commit()
    #     self.connect.close()
    #     return self.user_list

    def on_start(self):

        # self.run_sql()
        self.cursor = pymysql.connect(
            host='tidb.uat.etcp.net', port=5000, user='parking_dev', password='fTg1DIUKb81#tP3#', db='parking'
        )
        # self.cursor = self.client.cursor()

    def on_stop(self):

        print("------ Test over ------")  # 执行完测试任务后运行一次

    @task
    def execute_sql(self):

        # path = "execute_sql"
        # self.client.post(path, verify=False)
        try:
            sql = "SELECT id, plate_number, entrance_time, exit_time, receivable_fee, remarks FROM parking_record WHERE plate_number = '渝B52V96';"
            self.cursor.execute(sql)
            self.client.commit()
            res = self.cursor.fetchone()
            print(res)
            self.cursor.close()

        except:
            pass


class Tidb_Run_Set(User):
    tasks = [TidbTaskSet]
    min_wait = 1000
    max_wait = 3000
    host = 'tidb.uat.etcp.net'
