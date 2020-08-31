import pytest

from pages.app import BaseTest

'''
测试群体事件预警 pass
'''
class TestGroupWarning():
    def setup(self):
        self.app = BaseTest()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.close()

    #查看预警详情 群体事件预警-管理员帐号登录
    def test_group_warning_detail(self):
        memname,memidcard = self.main.login("00000","000000").goto_groupwarning_detail().goto_member_archive().get_member_info()
        print(memname,memidcard)





