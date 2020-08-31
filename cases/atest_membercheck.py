import pytest
import hamcrest

from pages.app import BaseTest

'''
测试人员核查 pass
'''
class TestMemberCheck():
    def setup(self):
        self.app = BaseTest()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.close()
# 搜索人员
    def test_search(self):
        result = self.main.login("01004","000000").goto_check().search_2("412000123456789004")
        assert result