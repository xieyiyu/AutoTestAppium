from base.base_parametrize import ParametrizedTestCase
from testpage.folder_rename_page import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class FolderRenameTest(ParametrizedTestCase):
    def test_folder_rename(self):
        folder_rename = FolderRename(driver=self.driver, path=PATH("../yamls/testyaml/folder_rename.yaml"))
        folder_rename.operate()

    def setUp(self):
        ("---------------FolderRenameTest---------------")
        super(FolderRenameTest, self).setUp()