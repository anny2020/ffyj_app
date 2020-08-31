import pytest
import hamcrest

from pages.app import BaseTest

'''
测试人员档案 pass
'''
class TestMemberArchive():
    def setup(self):
        self.app = BaseTest()
        self.main = self.app.start().main()


    def teardown(self):
        self.app.close()
# 搜索人员-需admin
    def test_search(self):
        result = self.main.login("00000","000000").goto_archive().search("412000123456789004")
        assert result