import  requests
from fake_useragent import UserAgent
ua = UserAgent()
json = {"token": 432424, "problem": "HCk", "cpu": 3, "memory": 5}
url = "https://watchdogserver.herokuapp.com/HealthChecker"
requests.post(url=url,json=json, headers={'user-agent': f'{ua.random}'}))

