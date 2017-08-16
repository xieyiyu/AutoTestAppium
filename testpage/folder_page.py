from base.base_operate import BaseOperate
from utils.yaml_util import get_yaml

class FolderPage:
    def __init__(self, **kwargs): # **kwargs表示关键字参数，是一个dict
        self.driver = kwargs['driver']
        self.path = kwargs['path']
        self.operate_element = BaseOperate(self.driver)
        self.is_operate = True
        self.test_info = get_yaml(self.path)['testinfo']
        self.test_case = get_yaml(self.path)['testcase']

    # 操作步骤
    def operate(self):
        for item in self.test_case:
            result = self.operate_element.operate(item,self.test_info)
            if not result:
                print("operate failed")
                self.is_operate = False
                break