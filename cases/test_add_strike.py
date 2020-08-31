import allure
import pytest
import yaml

from pages.app import BaseTest
from hamcrest import assert_that,contains_string

'''
测试打击处理
'''
@allure.feature('处理管理')
class TestAddStrike():
    def setup(self):
        self.app = BaseTest()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.close()

    @allure.story('新增处理')
    # @pytest.mark.skip("cannot take pictures")
    @pytest.mark.parametrize(['username','passwd','user_idcard','reason','remarks','tips'],
                             yaml.safe_load(open("../datas/data.yml",encoding='utf-8'))['strike'])
    def test_add_strike(self,username,passwd,user_idcard,reason,remarks,tips):
        result = self.main.login(f"{username}",f"{passwd}").goto_strike().search(f"{user_idcard}").strike().type()\
        .reason(f"{reason}").remarks(f"{remarks}").photo().submit().get_toast()
        assert_that(result,contains_string(f"{tips}"))

