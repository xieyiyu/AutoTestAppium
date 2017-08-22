from utils.apk_util import *
from utils.adb_util import *
from utils.yaml_util import get_yaml

# 获取文件绝对路径, 待改进：写在公共方法中
# os.path.abspath返回绝对路径，os.path.dirname返回文件路径，os.path.join(path1[,path2])将目录和文件名合成一个路径
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def init_devices():
    """
    初始化设备信息，添加指定apk路径，包名，主activity
    :return: device_config 设备信息
    """
    device_config = get_yaml(PATH("../yamls/config/config.yaml"))['devices']
    apk_path = get_yaml(PATH("../yamls/config/config.yaml"))['apk']
    apk_info = ApkUtil(apk_path).get_apk_info()
    get_devices = AdbUtil().get_device_list()
    i = 0
    for item in device_config:
        item['platformVersion'] = AdbUtil(get_devices[i]).get_android_version()
        item['deviceName'] = get_devices[i]
        item['udid'] = get_devices[i]
        item['app'] = apk_path
        item['appPackage'] = apk_info['appPackage']
        item['appActivity'] = apk_info['appActivity']
        i = i+ 1
    return device_config

if __name__ == '__main__':
    print(init_devices())