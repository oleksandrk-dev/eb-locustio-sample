from locust import HttpUser, task, constant_throughput


class QuickstartUser(HttpUser):
    wait_time = constant_throughput(1)

    @task
    def landing_page(self):
        self.client.get("/us/en/philippines")
