import allure
import yaml
import hamcrest

from pages.app import BaseTest
from hamcrest import assert_that,contains_string
import pytest
'''
测试核查
'''

@allure.feature('核查管理')
class TestGroupWarning():
    def setup(self):
        self.app = BaseTest()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.close()

    @allure.story('新增核查')
    @pytest.mark.parametrize(['username','passwd','user_idcard','place','detailed_place','described','tips'],
                             yaml.safe_load(open("../datas/data.yml",encoding='utf-8'))['check_report'])
    def test_check_report(self,username,passwd,user_idcard,place,detailed_place,described,tips):
        result = self.main.login(f"{username}",f"{passwd}").goto_check_report().search(f"{user_idcard}").check_report()\
        .place(f"{place}").detailed_place(f"{detailed_place}").handle().situation_described(f"{described}").submit().get_toast()
        assert_that(result,contains_string(f"{tips}"))

