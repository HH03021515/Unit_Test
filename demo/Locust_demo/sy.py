from locust import FastHttpUser, constant
from locust.user import task


class SyDividerUser(FastHttpUser):
    wait_time = constant(0.1)
    # host = 'http://cgateway.common.uat.etcp.net/'  # uat环境
    host = 'http://cgateway.common.prod.etcp.net/'  # 生产环境

    @task
    def state(self):
        with self.client.get(f'carInfoCheck/query', catch_response=True) as response:
            if response.json()['code'] != 0:
                response.failure('got wrong response')
