import os
import threading
from multiprocessing import Process
import urllib.request
from urllib.error import URLError

'''
启动、关闭、重启Appium服务
'''

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class BaseAppium:
    def __init__(self, devices):
        self.devices = devices

    # 启动appium服务
    def start_server(self):
        for i in range(0, len(self.devices)):
            print("---------------appium_start_server---------------")
            print(self.devices)
            device_config = self.devices[i]
            print(device_config)
            appium_cmd = "appium -a 127.0.0.1 -p " + str(device_config['port']) \
                         + " -bp " + str(device_config['bsport']) \
                         + " -U " + str(device_config['udid']) \
                         + " --session-override" \
                         + " --no-reset"
            print(appium_cmd)
            run_server = RunServer(appium_cmd)
            p = Process(target=run_server.start())
            p.start()

    # 关闭appium服务
    @staticmethod
    def stop_server():
        os.system('taskkill /f /im  node.exe')
        print("---------------appium_stop_server---------------")

    # 重启appium服务
    def restart_server(self):
        self.stop_server()
        self.start_server()
        print("---------------appium_restart_server---------------")

    # 判断appium服务是否开启
    def is_running(self):
        response = None
        for i in range(0, len(self.devices)):
            url = "http://127.0.0.1:" + str(self.devices[i]['port']) + "/wd/hub" + "/status"
            print("waiting to connect: ", url)
            try:
                response = urllib.request.urlopen(url, timeout=5)
                print("---------------appium_is_running_server---------------")
                print("response: ", response)
                if str(response.getcode()).startswith("2"):
                    return True
                else:
                    return False
            except URLError:
                return False
            finally:
                if response:
                    response.close()

class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        os.system(self.cmd)

if __name__ == '__main__':
    pass