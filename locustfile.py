import math
from collections import namedtuple

from locust import HttpUser, task, constant_throughput, TaskSet, constant, LoadTestShape, constant_pacing


# preprod: https://preprod.dev.remitly.com
class UserTasks(TaskSet):
    @task
    def get_url(self):
        response = self.client.get("/us/en/india")
        self.client.cookies.clear()


class WebsiteUser(HttpUser):
    wait_time = constant_throughput(50)
    # stop_timeout = 20
    tasks = [UserTasks]

