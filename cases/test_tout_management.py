import allure
import pytest
import yaml

from pages.app import BaseTest
from hamcrest import assert_that, contains_string, equal_to

'''
测试新增撤管 pass
'''
@allure.feature('撤管管理')
class TestTarget:

    def setup(self):
        self.app = BaseTest()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.close()

    @allure.story("新增")
    @pytest.mark.parametrize(['username','passwd','user_idcard','reason','tips'],
                             yaml.safe_load(open('./datas/data.yml',encoding='utf-8'))['out_management'])
    def test_out_management(self,username,passwd,user_idcard,reason,tips):
        result = self.main.login(f"{username}",f"{passwd}").goto_out_manage().search(f"{user_idcard}").add_out_management()\
            .select_reason().input_comments(f"{reason}").click_submit().get_toast()
        assert_that(result,contains_string(f"{tips}"))

    @allure.story("所长审批")
    @pytest.mark.parametrize(["username","passwd","comments","assert_content"],
                             yaml.safe_load(open("./datas/data.yml",encoding='utf-8'))['add_approve_1'])
    def test_out_management_approve_agree(self,username,passwd,comments,assert_content):
        result = self.main.login(f"{username}",f"{passwd}").goto_unchecked().goto_approve_detail().input_comments(f"{comments}")\
            .click_complete().get_toast()
        assert_that(result,contains_string(f"{assert_content}"))

    @allure.story("局长审批")
    @pytest.mark.parametrize(["username", "passwd", "comments", "assert_content"],
                             yaml.safe_load(open("./datas/data.yml", encoding='utf-8'))['add_approve_2'])
    def test_out_management_approve_disagree(self,username,passwd,comments,assert_content):
        result = self.main.login(f"{username}",f"{passwd}").goto_unchecked().goto_approve_detail()\
            .input_comments(f"{comments}").click_complete().get_toast()
        assert_that(result,contains_string(f"{assert_content}"))

