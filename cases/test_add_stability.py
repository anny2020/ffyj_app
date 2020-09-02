import allure
import hamcrest
import pytest
import yaml

from pages.app import BaseTest

'''
测试稳控工作 pass
'''
@allure.feature('稳控管理')
class TestAddStability:
    def setup(self):
        self.app = BaseTest()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.close()

    @allure.story('新增稳控')
    @pytest.mark.parametrize(['username','passwd','user_idcard','place','describe','behaviour','remarks','tips'],
                             yaml.safe_load(open("../datas/data.yml",encoding='utf-8'))['stability'])
    def test_add_stability(self,username,passwd,user_idcard,place,describe,behaviour,remarks,tips):
        result = self.main.login(f"{username}",f"{passwd}").goto_StabilityControl().search(f"{user_idcard}")\
            .add_StabilityControl().type().status().place(f"{place}").describe(f"{describe}").behaviour(f"{behaviour}")\
            .remarks(f"{remarks}").submit().get_toast()
        hamcrest.assert_that(result,hamcrest.contains_string(f"{tips}"))


