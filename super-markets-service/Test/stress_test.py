from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    @task
    def get_partner_shops(self):
        myjson = {'id': '2810501', 'ingredients': ['butter', 'brown sugar', 'apple juice', 'flour', 'baking powder', 'salt', 'white sugar', 'egg','mustard', 'ketchup', 'paprika']}
        self.client.post("/getShops", json=myjson)

    @task
    def tst(self):
        myjson = {'id': '1', 'ingredients': ['blueberry', 'cinnamon', 'pineapple']}
        self.client.post("/getSuperMarketDetails", json=myjson)

    @task
    def not_exists(self):
        self.client.post("/notExists")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 500
    max_wait = 750
    # 300 , 10