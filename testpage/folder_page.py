from base.base_operate import BaseOperate
from utils.yaml_util import get_yaml
from utils.logging_config import log

class FolderPage:
    def __init__(self, **kwargs): # **kwargs表示关键字参数，是一个dict
        self.driver = kwargs['driver']
        self.path = kwargs['path']
        self.operate_element = BaseOperate(self.driver)
        self.is_operate = True
        self.test_info = get_yaml(self.path)['testinfo']
        self.test_case = get_yaml(self.path)['testcase']

    # 操作步骤
    def operate(self, test_case_name):
        case = self.test_case[test_case_name]
        for item in case:
            result = self.operate_element.operate(item,self.test_info)
            if not result:
                log.error("operate s% failed", item)
                self.is_operate = False
                break