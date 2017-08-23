import re
import subprocess
import os
import math
from utils.logging_util import log

'''
获取apk信息
'''
class ApkUtil:
    def __init__(self, apk_path):
        self.apk_path = apk_path

    def aapt(self, args):
        """
        aapt命令
        :param args:
        :return:
        """
        cmd = "aapt %s" % (str(args))
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def get_apk_info(self):
        """
        获取app包名,versionCode,versionName,应用名称
        :return: apk_info
        """
        args = "dump badging %s" % self.apk_path
        result = self.aapt(args).stdout.read().strip().decode()
        match_package = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(result)
        if not match_package:
            raise Exception("can't get app_package_info")

        match_activity = re.compile("launchable-activity: name='(\S+)'").search(result) # 获取app主activity
        if not match_activity:
            raise Exception("can't get app_activity_info")

        match_name = re.compile("application-label:(\S+)").search(result)
        if not match_name:
            raise Exception("can't get app_name_info")

        apk_info = dict()
        apk_info['appPackage'] = match_package.group(1)
        apk_info['versionCode'] = match_package.group(2)
        apk_info['versionName'] = match_package.group(3)
        apk_info['appActivity'] = match_activity.group(1)
        apk_info['appName'] = match_name.group(1)
        return apk_info

    def get_apk_size(self):
        """
        获取apk大小
        :return: apk_size
        """
        apk_size = math.floor(os.path.getsize(self.apk_path) / (1024 * 1000))
        return str(apk_size) + "M"


if __name__ == '__main__':
    pass
    apk_info1 = ApkUtil(r"D:\workspace\PycharmProjects\AutoTestAppium\yamls\config\CLauncher-release.apk").get_apk_info()
    print(apk_info1)
    log.info(apk_info1)
    log.info(ApkUtil(r"D:\workspace\PycharmProjects\AutoTestAppium\yamls\config\CLauncher-release.apk").get_apk_size())

