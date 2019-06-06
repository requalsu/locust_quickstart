from locust import HttpLocust, TaskSet, task
import random

USERNAME = 'userName'
PASSWORD = 'passWord'


class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/pf/login/userLogin.do",
                         {USERNAME: 'fa1', PASSWORD: "1", 'datetimepickerValue': '2019-06-06'})

    def logout(self):
        self.client.get("/pf/login/loginOut.do")
    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def getlist(self):
        self.client.get("/fa/card/sysEdit/getList")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    # min_wait = 1000
    # max_wait = 5000
    wait_function = lambda self: random.expovariate(1) * 1000    # 对于指数分布的等待时间平均为1秒
    host = 'http://10.10.65.240:9999'
