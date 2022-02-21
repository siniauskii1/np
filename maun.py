import  requests
from fake_useragent import UserAgent
ua = UserAgent()
url = "https://watchdogserver.herokuapp.com/HealthChecker"
requests.post(url=url,headers={'user-agent': f'{ua.random}'}))

