from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet) :
    #def on_start(self):
        #self.client.post("/getLocalization")

    #@task
    #def index(self):
        #self.client.get("/")

    @task
    def about(self):
        self.client.get("/getLocalization")

class WebsiteUser(HttpLocust) :
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 1500