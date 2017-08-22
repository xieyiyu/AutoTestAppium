import unittest
from appium import webdriver
from utils.logging_config import log

'''
参数化测试用例
'''

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    devices = dict()
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        global devices
        devices = param

    @classmethod
    def setUpClass(cls):
        global devices
        desired_caps = dict()
        desired_caps['platformName'] = devices['platformName']
        desired_caps['platformVersion'] = devices['platformVersion']
        desired_caps['deviceName'] = devices['deviceName'] # 暂未添加获取deviceName方法，用udid替代
        desired_caps['udid'] = devices['udid']
        desired_caps['app'] = devices['app']
        desired_caps['appPackage'] = devices['appPackage']
        desired_caps['appActivity'] = devices['appActivity']
        desired_caps['noReset'] = "true"
        desired_caps['fullReset'] = "false"

        remote = "http://127.0.0.1:" + str(devices['port']) + "/wd/hub"
        cls.driver = webdriver.Remote(remote, desired_caps)

    @staticmethod
    def parametrize(testcase_klass, param=None):
        log.info('testcase_klass: ', testcase_klass)
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite