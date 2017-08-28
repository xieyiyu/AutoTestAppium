from utils.logging_util import log
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
        重写元素定位方法
        :param case_operate: 用例操作
        :return:
        """
        try:
            if type(case_operate) == list: # 多个元素
                for item in case_operate:
                    WebDriverWait(self.driver, BaseElement.WAIT_TIME).until(lambda x: self.find_element_by(item))
                return True
            if type(case_operate) == dict: # 单个元素
                WebDriverWait(self.driver, BaseElement.WAIT_TIME).until(lambda x: self.find_element_by(case_operate))
                return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def operate(self, case_operate, test_info):
        """
        封装元素操作方法
        :param case_operate: 用例操作
        :param test_info: 测试套件信息
        :return:
        """
        log.info('----------------base_operate---------------')
        log.info('test_info: %s' % test_info)
        elements = {
            BaseElement.CLICK: lambda: self.click(case_operate),
            BaseElement.SET_VALUE: lambda: self.set_value(case_operate),
            BaseElement.SWIPE_LEFT: lambda: self.swipe_left(case_operate),
            BaseElement.SWIPE_RIGHT: lambda: self.swipe_right(case_operate),
            BaseElement.SWIPE_UP: lambda: self.swipe_up(case_operate),
            BaseElement.SWIPE_DOWN: lambda: self.swipe_down(case_operate),
            BaseElement.KEY_EVENT: lambda: self.key_event(case_operate)
        }
        if case_operate.__contains__('element_info'): # 没有element_info这个键，不查找元素，直接执行
            if self.find_element(case_operate):
                elements[case_operate['operate_type']]()
                return True
            return False
        else:
            elements[case_operate['operate_type']]()
            return True


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

    def click(self, case_operate):
        """
        元素点击事件
        """
        self.find_element_by(case_operate).click() # 此处应添加判断testcase['find_type']是否是BaseElement类中定义的类型之一
        log.info("click %s" % case_operate)

    def set_value(self, case_operate):
        """
        设置值
        """
        self.find_element_by(case_operate).set_value(case_operate["text"])
        log.info("set %s" % case_operate["text"])

    def get_window_size(self):
        """
        获取屏幕分辨率
        :return: width*height
        """
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width,height

    def swipe_to(self, x1, y1, x2, y2, times, swipe_time):
        """
        滑动屏幕
        :param x1: 起点横坐标
        :param y1: 起点纵坐标
        :param x2: 重点横坐标
        :param y2: 终点纵坐标
        :param times: 滑动次数
        :param swipe_time: 滑动时间
        :return:
        """
        width, height = self.get_window_size()
        for i in range(times):
            self.driver.swipe(width * x1, height * y1, width * x2, height * y2, swipe_time)
            sleep(1)

    def swipe_left(self, case_operate):
        """
        左滑
        """
        self.swipe_to(0.8, 0.5, 0.2, 0.5, case_operate['times'], case_operate['swipe_time'])

    def swipe_right(self, case_operate):
        """
        右滑
        """
        self.swipe_to(0.2, 0.5, 0.8, 0.5, case_operate['times'], case_operate['swipe_time'])

    def swipe_up(self, case_operate):
        """
        上滑
        """
        self.swipe_to(0.5, 0.8, 0.5, 0.2, case_operate['times'], case_operate['swipe_time'])

    def swipe_down(self, case_operate):
        """
        下滑
        """
        self.swipe_to(0.5, 0.2, 0.5, 0.8, case_operate['times'], case_operate['swipe_time'])

    def key_event(self, case_operate):
        """
        操作实体按键
        按键码参考链接http://blog.csdn.net/qq_22795513/article/details/53169593
        :return:
        """
        log.info("key_event: " % case_operate)
        self.driver.keyevent(case_operate['key_code'])

