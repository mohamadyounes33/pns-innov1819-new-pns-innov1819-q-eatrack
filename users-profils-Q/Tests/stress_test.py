from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet) :

    @task
    def about(self):
        #self.client.post("getUserProfil?userID=675719")
        #self.client.post("/getUserProfil?userID=675719")
        myjson = {'userID' : '675719'}
        self.client.post("/getUserProfil?userID",json=myjson)

    @task
    def not_exists(self):
        self.client.post("/notExists")


class WebsiteUser(HttpLocust) :
    task_set = WebsiteTasks
    min_wait = 500
    max_wait = 750
    #300 , 10