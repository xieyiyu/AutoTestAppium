from utils.logging_util import log
from pageobejct.base_operate import BaseOperate
from utils.yaml_util import get_yaml

class BaseCase:
    def __init__(self, **kwargs): # **kwargs表示关键字参数，是一个dict
        self.driver = kwargs['driver']
        self.path = kwargs['path']
        self.operate_element = BaseOperate(self.driver)
        self.is_operate = True
        self.test_info = get_yaml(self.path)['testinfo']
        self.test_case = get_yaml(self.path)['testcase']

    def operate(self, test_case_name):
        """
        操作步骤
        :param test_case_name: 用例名称 对应yaml中
        :return:
        """
        case = self.test_case[test_case_name]
        for item in case:
            result = self.operate_element.operate(item,self.test_info)
            if not result:
                log.error("operate %s failed" % item)
                self.is_operate = False
                break

    def check_point(self):
        """
        检查点
        :return:
        """
        result = False
        if not self.is_operate:
            log.error("operate failed,can't find check_point")
        else:
            check = get_yaml(self.path)['check']
            result = self.operate_element.find_element(check)
