import os

from base.base_parametrize import ParametrizedTestCase
from testpage.folder_page import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class FolderTest(ParametrizedTestCase):

    def test_01_folder_rename(self):
        self.folder = FolderPage(driver=self.driver, path=PATH("../yamls/testyaml/folder.yaml"))
        self.folder.operate(test_case_name='folder_rename')


    def test_02_folder_create(self):
        self.folder = FolderPage(driver=self.driver, path=PATH("../yamls/testyaml/folder.yaml"))
        self.folder.operate(test_case_name='folder_create')

    def setUp(self):
        super(FolderTest, self).setUp()