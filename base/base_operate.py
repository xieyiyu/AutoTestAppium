from base.base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions

class BaseOperate:
    def __init__(self, driver=""):
        self.driver = driver

    # 查找元素
    def find_element(self, case_operate):
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
    def operate(self, case_operate, test_info, log_test): # 未写入log
        if self.find_element(case_operate):
            elements = {
                BaseElement.CLICK: lambda: self.click(case_operate),
                BaseElement.SWIPE_LEFT: lambda: self.swipe_left(case_operate)
            }
            elements[case_operate['operate_type']]()
            return True
        return False

    # 点击事件
    def click(self, testcase):
        self.find_element_by(testcase).click() # 此处应添加判断testcase['find_type']是否是BaseElement类中定义的类型之一

    # 左滑动
    def swipe_left(self, case_operate, swipe_time):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        for i in range(case_operate['times']):
            self.driver.swipe(width * 0.75, height * 0.5, width * 0.25, height * 0.5, swipe_time)

    # 封装常用查找元素方法
    def find_element_by(self, case_operate):
        elements = {
            BaseElement.find_element_by_id: lambda: self.driver.find_element_by_id(case_operate['element_info']),
            BaseElement.find_element_by_name: lambda: self.driver.find_element_by_name(case_operate['element_info']),
            BaseElement.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(case_operate['element_info']),
            BaseElement.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(case_operate['element_info'])
        }
        return elements[case_operate['find_type']]()