import time
import datetime
import unittest
import utils.HTMLTestRunner

from utils.adb_util import *
from base.base_appium import *
from base.base_init import init_devices
from multiprocessing import Pool

def runner_pool(devices_pool):
    print("---------------runner_pool---------------")
    print(devices_pool)
    pool = Pool(len(devices_pool))  # 创建进程池，设置最大进程数量
    print(pool)
    # pool.map(runner_case_app, devices_pool)
    # pool.close()  # 等待进程池中的worker进程执行结束再关闭pool
    # pool.join()  # 等待进程池中的worker进程执行完毕，防止主进程在worker进程结束前结束，必须在close()或terminate()之后

def runner_case_app(devices_app):
    print("---------------runner_case_app---------------")
    start_time = datetime.now()
    suite = unittest.TestSuite()


if __name__ == '__main__':
    if AdbUtil().adb_devices():
        get_devices = init_devices()
        appium_server = BaseAppium(get_devices)
        appium_server.start_server()
        while not appium_server.is_running():
            time.sleep(5)
        runner_pool(get_devices)
        appium_server.stop_server()
    else:
        print(u"设备不存在")

