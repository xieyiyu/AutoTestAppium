import os

from base.base_parametrize import ParametrizedTestCase
from testpage.folder_page import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class FolderTest(ParametrizedTestCase):
    def test_01_folder_rename(self):
        folder_rename = FolderPage(driver=self.driver, path=PATH("../yamls/testyaml/folder.yaml"))
        folder_rename.operate()

    # def test_02_folder_create(self):
    #     folder_create = FolderPage(driver=self.driver, )

    # def setUp(self):
    #     ("---------------FolderRenameTest---------------")
    #     super(FolderRenameTest, self).setUp()