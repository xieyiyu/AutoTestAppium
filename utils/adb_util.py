import os

'''
adb 命令
'''

class AdbUtil(object):
    @staticmethod
    def call_adb(command):
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r") # 从一个命令中打开一个管道
        while 1:
            line = results.readline()
            if not line:
                break
            command_result += line
        results.close()
        return command_result

    # 检查设备,adb devices
    def adb_devices(self):
        result = self.call_adb("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice') # ['device1', 'device2', '']
        # 此处存在问题，若device状态为offline或其它，则无法分割字符串，待解决
        devices.pop() # 删除最后一个空元素，得到设备的list
        print(len(devices),'devices: ', devices)
        return devices

if __name__ == '__main__':
    if AdbUtil().adb_devices():
        print(u"设备存在")
    else:
        print(u"设备不存在")
