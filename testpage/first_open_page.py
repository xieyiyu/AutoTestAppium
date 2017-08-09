from base.base_operate import BaseOperate
from utils.yaml_util import get_yaml

class FirstOpen:
    def __init__(self, **kwargs): # **kwargs表示关键字参数，是一个dict
        self.driver = kwargs['driver']
        self.path = kwargs['path']
        self.