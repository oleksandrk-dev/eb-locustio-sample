from locust import HttpUser, task, constant_throughput


class QuickstartUser(HttpUser):
    wait_time = constant_throughput(1)

    @task(3)
    def landing_page1(self):
        self.client.get("/us/en/philippines")

    @task(3)
    def landing_page2(self):
        self.client.get("/us/es/méxico")

    @task(3)
    def landing_page3(self):
        self.client.get("/ca/en/india")

    @task(3)
    def landing_page4(self):
        self.client.get("/us/en/pakistan")