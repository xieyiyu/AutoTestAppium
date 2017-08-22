from time import sleep
import selenium.common.exceptions
from selenium.webdriver.support.ui import WebDriverWait

from pageobejct.base_element import BaseElement

"""
所有元素操作方法
"""

class BaseOperate:
    def __init__(self, driver=""):
        self.driver = driver

    def find_element(self, case_operate):
        """
        查找元素是否存在
        :param case_operate: 用例操作
        :return:
        """
        try:
            if type(case_operate) == list: # 多检查点
                for item in case_operate:
                    WebDriverWait(self.driver, BaseElement.WAIT_TIME).until(lambda x: self.find_element_by(item))
                return True
            if type(case_operate) == dict: # 单检查点
                WebDriverWait(self.driver, BaseElement.WAIT_TIME).until(lambda x: self.find_element_by(case_operate))
                return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            print("can't find element")
            return False

    # 封装操作
    def operate(self, case_operate, test_info): # 未写入log
        """
        封装元素操作方法
        :param case_operate: 用例操作
        :param test_info: 测试套件信息
        :return:
        """
        print('----------------base_operate---------------')
        print('test_info: ',test_info)
        if self.find_element(case_operate):
            elements = {
                BaseElement.CLICK: lambda: self.click(case_operate),
                BaseElement.SWIPE_LEFT: lambda: self.swipe_left(case_operate),
                BaseElement.SET_VALUE: lambda : self.set_value(case_operate)
            }
            elements[case_operate['operate_type']]()
            return True
        return False

    def click(self, case_operate):
        """
        元素点击事件
        """
        self.find_element_by(case_operate).click() # 此处应添加判断testcase['find_type']是否是BaseElement类中定义的类型之一

    def set_value(self, case_operate):
        """
        设置值
        """
        self.find_element_by(case_operate).set_value(case_operate["text"])

    # 左滑动
    def swipe_left(self, case_operate):
        """
        左滑动
        """
        width = self.driver.get_window_size()['width'] # 待改进：获取window_size应封装
        height = self.driver.get_window_size()['height']
        for i in range(case_operate['times']):
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, case_operate['swipe_time'])
            sleep(1)

    def swipe_right(self, case_operate):
        """
        右滑动
        """
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        for i in range(case_operate['times']):
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, case_operate['swipe_time'])
            sleep(1)

    def find_element_by(self, case_operate):
        """
        封装常用元素定位方法
        """
        elements = {
            BaseElement.find_element_by_id: lambda: self.driver.find_element_by_id(case_operate['element_info']),
            BaseElement.find_element_by_name: lambda: self.driver.find_element_by_name(case_operate['element_info']),
            BaseElement.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(case_operate['element_info']),
            BaseElement.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(case_operate['element_info'])
        }
        return elements[case_operate['find_type']]()