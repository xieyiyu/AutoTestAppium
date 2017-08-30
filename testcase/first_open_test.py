import os

from base.base_parametrize import ParametrizedTestCase
from base.base_case_operate import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class FirstOpenTest(ParametrizedTestCase):
    def test_01_first_open(self): # 方法命名要以test_开头
        self.first_open.operate(test_case_name='first_open')
        self.first_open.check_point()

    # def test_02(self):
    #     self.first_open.operate(test_case_name='zoom_test')

    def setUp(self):
        super(FirstOpenTest, self).setUp()
        self.first_open = BaseCase(driver=self.driver, path=PATH("../yamls/testyaml/first_open.yaml"))