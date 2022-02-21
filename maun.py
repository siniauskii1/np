import  requests
print("DOLBAEB")
url = "https://watchdogserver.herokuapp.com/HealthChecker"
while True:
    requests.post(url)


