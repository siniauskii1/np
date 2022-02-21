import requests
r = requests.post(url = "https://watchdogserver.herokuapp.com/HealthChecker")
print(r.status_code)
