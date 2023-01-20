from locust import task, TaskSet


class UserTasks(TaskSet):
    @task
    def get_url(self):
        self.client.get("/us/en/india")
        self.client.cookies.clear()
