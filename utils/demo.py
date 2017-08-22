import os
import re
import math
from math import ceil
import subprocess

'''
adb 命令
'''

class AdbUtil(object):
    def __init__(self, device_id=""):
        if device_id == "":
            self.device_id = ""
        else:
            self.device_id = "-s %s" % device_id

    def adb(self, args):
        """
        adb命令
        """
        cmd = "adb %s %s" % (self.device_id, str(args)) # 单个设备可不传入device_id
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def get_device_state(self):
        """
        获取设备当前状态： device | offline | 其它
        :return: state 设备状态
        """
        return self.adb("get-state").stdout.read().strip().decode()

    def get_device_id(self):
        """
        获取设备id
        :return: serialNo 设备id
        """
        return self.adb("get-serialno").stdout.read().strip().decode()

    def get_devices(self):
        """
        获取连接的所有在线设备
        :return:  devices_list 设备id列表
        """
        devices_list = list()
        for b in self.adb("devices").stdout.readlines():
            device = bytes.decode(b)
            if 'device' in device and 'devices' not in device:
                device = device.split('\t')[0]
                devices_list.append(device)
        return devices_list

    def get_android_version(self):
        """
        获取设备的Android版本号
        :return: android_version 安卓版本号
        """
        return self.adb("shell getprop ro.build.version.release").stdout.read().strip().decode()

    def get_device_model(self):
        """
        获取设备型号
        :return: device_model 设备型号
        """
        return self.adb("shell getprop ro.product.model").stdout.read().strip().decode()

    def get_device_brand(self):
        """
        获取设备品牌
        :return: device_brand 设备品牌
        """
        return self.adb("shell getprop ro.product.brand").stdout.read().strip().decode()

    def get_device_name(self):
        """
        获取设备名称
        :return: device_name 设备名称
        """
        return self.adb("shell getprop ro.product.device").stdout.read().strip().decode()

    def install_app(self, apk_path):
        """
        安装app
        :param apk_path: apk路径
        :return:
        """
        return self.adb("install -r %s" % apk_path)

if __name__ == '__main__':
    print(AdbUtil().get_devices())
    print(AdbUtil().get_android_version())
    print(AdbUtil().get_device_model(), AdbUtil().get_device_brand(), AdbUtil().get_device_name())


