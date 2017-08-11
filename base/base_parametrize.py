import unittest
from appium import webdriver
'''
参数化测试用例
'''

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.devices = param

    def setUp(self):
        desired_caps = dict()
        desired_caps['platformName'] = self.devices['platformName']
        desired_caps['platformVersion'] = self.devices['platformVersion']
        desired_caps['deviceName'] = self.devices['udid'] # 暂未添加获取deviceName方法，用udid替代
        desired_caps['app'] = self.devices['app']
        desired_caps['appPackage'] = self.devices['appPackage']
        desired_caps['appActivity'] = self.devices['appActivity']

        remote = "http://127.0.0.1:" + str(self.devices['port']) + "/wd/hub"
        self.driver = webdriver.Remote(remote, desired_caps)

    @staticmethod
    def parametrize(testcase_klass, param=None):
        print('testcase_klass: ', testcase_klass)
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite