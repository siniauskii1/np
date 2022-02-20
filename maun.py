
import  requests
json = {"token": 432424, "problem": "HCk", "cpu": 3, "memory": 5}
url = "https://watchdogserver.herokuapp.com/HealthChecker"
requests.post(url,json)

