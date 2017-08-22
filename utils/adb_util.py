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
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r") # 从一个命令中打开一个管道，执行adb命令,并返回结果
        while 1:
            line = results.readline() # read可看到执行的输出
            if not line:
                break
            command_result += line
        results.close()
        return command_result

    # 检查设备,adb devices,获取连接的设备
    def adb_devices(self):
        result = self.call_adb("devices")
        print(result)
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice') # ['device1', 'device2', '']
        # 此处存在问题，若device状态为offline或其它，则无法分割字符串，待解决
        devices.pop() # 删除最后一个空元素，得到设备的list
        print(len(devices),'devices: ', devices)
        return devices

    #
    def adb_get_phone_info(self):
        pass

if __name__ == '__main__':
    if AdbUtil().adb_devices():
        print(u"设备存在")
    else:
        print(u"设备不存在")
