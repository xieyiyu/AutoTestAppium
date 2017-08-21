import os
import re
import math
from math import ceil
import subprocess

'''
adb 命令
'''

class AdbUtil(object):
    @staticmethod
    def call_adb(command):
        cmd = "adb %s "  % command
        result = os.popen(cmd, "r").readlines()
        return result

    # 检查设备,adb devices,获取连接的设备
    def adb_devices(self):
        result = self.call_adb("devices")
        result.pop(0)
        print(result)
        device = []
        for i in result:
            j=0
            device[j] = i.split('\tdevice')
            print(device)
            j = j+1
        device.pop() # 删除最后一个空元素，得到设备的list
        print(len(device),'devices: ', device)
        return device

if __name__ == '__main__':
    if AdbUtil().adb_devices():
        print(u"设备存在")
    else:
        print(u"设备不存在")
