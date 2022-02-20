import psutil
import requests,time, subprocess
import threading
from time import sleep
from subprocess import Popen
from fake_useragent import UserAgent
ua = UserAgent()

class WatchDog:

    url = "http://127.0.0.1:8080/HealthChecker"
    def __init__(self, token):
        self.token = token

    def __health_checker(self,dir):
        LastTime = time.time()
        psutil.cpu_percent()
        while True:
            if time.time()-LastTime>5:
                cpu = psutil.cpu_percent()
                memory = psutil.virtual_memory()
                print(cpu,memory)
                json = {"token" : self.token,  "problem" : "HCk", "cpu" : cpu, "memory" : memory.percent}

                response = requests.post(url=self.url,
                                         json=json,
                                         headers={'user-agent': f'{ua.random}'})
                LastTime = time.time()
                print(response.status_code)

    def send_error(self, error):
        json = {"token": self.token, "problem": str(error)}
        r = requests.post(url=self.url,
                            json=json,
                            headers={'user-agent': f'{ua.random}'})
        print(f"Sended error with code: {str(r.status_code)}")

    def user_file(self, dir):
        code = False
        print(dir)

        if ".py" in dir:
            code = "python"
        elif ".js" in dir:
            code = "node"
        print(f"{str(code)} file was started")
        if code:
            try:
                subprocess.check_output([code, dir], stderr=subprocess.PIPE)
            except subprocess.CalledProcessError as e:
                print(e.stderr)
                self.send_error(e.stderr)


    def Start_watching(self, dir): #Основная функция
         thr1 = threading.Thread(target=self.__health_checker, args=[dir])
         thr1.daemon = 1
         thr1.start()
         self.user_file(dir)
         print("close")


class SerKep:

    url2 = "http://127.0.0.1:8080/CucleChecker"
    url3 = "http://127.0.0.1:8080/MakeLog"
    __lasttime = {}

    def __init__(self, token):
        self.token = token
        self.time = time.time()

    def make_log(self, info, tag = "INFO"):
        try:
            json = { "token" : self.token, "tag" : str(tag), "info" : str(info)}
            requests.post(url = self.url3,
                          json = json,
                          headers={'user-agent': f'{ua.random}'})
        except:
            pass

    def cucle_checker(self, name, limit = 10):
        try:
            if name in self.__lasttime:
                if(limit*60<=(time.time()-self.__lasttime[name])):
                    json = { "token" : self.token, "message" : "Cucle "+str(name)+" is running longer than the time limit, looping is possible"}
                    requests.post(url=self.url2,
                                  json=json,
                                  headers={'user-agent': f'{ua.random}'})
                    self.__lasttime[name] = time.time()+6000
            else:
                self.__lasttime[str(name)] = time.time()
        except:
            pass

    def erase_cucle_checker(self, name):
        try:
            if name in self.__lasttime:
                del self.__lasttime[str(name)]
        except:
            pass

    def erase_all_cucle_checker(self):
        try:
            self.__lasttime.clear()
        except:
            pass









