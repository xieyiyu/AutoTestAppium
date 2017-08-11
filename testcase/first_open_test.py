from base.base_parametrize import ParametrizedTestCase
from testpage.first_open_page import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class FirstOpenTest(ParametrizedTestCase):
    def test_first_open(self): # 方法命名要以test开头
        first_open = FirstOpen(driver=self.driver, path=PATH("../yamls/testyaml/first_open.yaml"))
        first_open.operate()

    def setUp(self):
        ("---------------FirstOpenTest---------------")
        super(FirstOpenTest, self).setUp()