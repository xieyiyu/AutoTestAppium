import re
import subprocess
import os
import math

'''
获取apk信息
'''
class ApkUtil:
    def __init__(self, apk_path):
        self.apk_path = apk_path

    # 获取apk信息
    def get_apk_info(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apk_path,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=True)
        (output, err) = p.communicate()
        #print(output.decode())
        # 获取app包名,versionCode,versionName
        match_package = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        print(match_package)
        if not match_package:
            raise Exception("can't get app_package_info")

        # 获取app主activity
        match_activity = re.compile("launchable-activity: name='(\S+)'").search(output.decode())
        # print(match_activity)
        if not match_activity:
            raise Exception("can't get app_activity_info")

        apk_info = dict()
        apk_info['appPackage'] = match_package.group(1)
        apk_info['versionCode'] = match_package.group(2)
        apk_info['versionName'] = match_package.group(3)
        apk_info['appActivity'] = match_activity.group(1)

        return apk_info

    # 获取apk大小
    def get_apk_size(self):
        apk_size = math.floor(os.path.getsize(self.apkPath) / (1024 * 1000))
        return str(apk_size) + "M"

if __name__ == '__main__':
    pass
    apk_info1 = ApkUtil(r"D:\workspace\PycharmProjects\AutoTestAppium\yamls\config\CLauncher-release.apk").get_apk_info()
    print(apk_info1)

