import os

from base.base_parametrize import ParametrizedTestCase
from testpage.first_open_page import *
from testpage.folder_page import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class FirstOpenTest(ParametrizedTestCase):
    def test_first_open(self): # 方法命名要以test_开头
        first_open = FirstOpen(driver=self.driver, path=PATH("../yamls/testyaml/first_open.yaml"))
        first_open.operate()
        first_open.check_point()

    def setUp(self):
        ("---------------FirstOpenTest---------------")
        super(FirstOpenTest, self).setUp()