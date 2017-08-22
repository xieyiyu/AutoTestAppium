from utils.apk_util import *
from utils.adb_util import *
from utils.yaml_util import get_yaml

'''
初始化设备信息
'''

# 获取文件绝对路径, 待改进：写在公共方法中
# os.path.abspath返回绝对路径，os.path.dirname返回文件路径，os.path.join(path1[,path2])将目录和文件名合成一个路径
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# 初始化设备信息，添加指定apk路径，包名，主activity
def init_devices():
    get_devices = get_yaml(PATH("../yamls/config/devices.yaml"))
    apk_path = get_yaml(PATH("../yamls/config/app.yaml"))["app"]
    apk_info = ApkUtil(apk_path).get_apk_info()
    get_devices_udid = AdbUtil().adb_devices()
    i = 0
    for item in get_devices:
        item['udid'] = get_devices_udid[i]
        item['app'] = apk_path
        item['appPackage'] = apk_info['appPackage']
        item['appActivity'] = apk_info['appActivity']
        i = i+ 1
    return get_devices

if __name__ == '__main__':
    init_devices()