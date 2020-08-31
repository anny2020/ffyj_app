import allure
import pytest
import yaml

from pages.app import BaseTest
from hamcrest import assert_that, contains_string, equal_to

'''
测试登记
'''
@allure.feature('登记管理')
class TestRegistration:

    def setup(self):
        self.app = BaseTest()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.close()

    @allure.story('新增登记')
    @pytest.mark.parametrize(['username','passwd','user_idcard','demands','tips'],
                             yaml.safe_load(open('./datas/data.yml',encoding='utf-8'))['registration'])
    def test_registration(self,username,passwd,user_idcard,demands,tips):
        result = self.main.login(f"{username}",f"{passwd}").goto_registration().search(f"{user_idcard}").registration()\
        .type().date().live_status().demands(f"{demands}").submit().get_toast()
        assert_that(result,contains_string(f"{tips}"))