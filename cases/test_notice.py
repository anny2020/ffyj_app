

import os

cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)

import allure
import pytest
import yaml

from pages.app import BaseTest
from hamcrest import assert_that, contains_string, equal_to
'''
测试通知 pass
'''

@allure.feature('通知管理')
class TestNoctice():

    def setup(self):
        self.app = BaseTest()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.close()

    @allure.story('删除全部通知')
    @pytest.mark.parametrize(['username','passwd','tips'],yaml.safe_load(open('../datas/data.yml',encoding='utf-8'))['notice'])
    def test_notice_all_detail(self,username,passwd,tips):
        result = self.main.login(f"{username}",f"{passwd}").goto_notices().all().remove_icon().select_remove()\
        .delete_btn().get_toast()
        assert_that(result,contains_string(f"{tips}"))

    @allure.story('删除已读通知')
    @pytest.mark.parametrize(['username','passwd','tips'], yaml.safe_load(open('../datas/data.yml',encoding='utf-8'))['notice'])
    def test_have_read_detial(self,username,passwd,tips):
        result = self.main.login(f"{username}",f"{passwd}").goto_notices().have_read().remove_icon().select_remove()\
            .delete_btn().get_toast()
        assert_that(result,contains_string(f"{tips}"))

    @allure.story('删除未读通知')
    @pytest.mark.parametrize(['username','passwd','tips'], yaml.safe_load(open('../datas/data.yml',encoding='utf-8'))['notice'])
    def test_unread_detail(self,username,passwd,tips):
        result = self.main.login(f"{username}",f"{passwd}").goto_notices().unread().remove_icon().select_remove()\
            .delete_btn().get_toast()
        assert_that(result,contains_string(f"{tips}"))
