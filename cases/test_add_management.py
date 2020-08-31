import hamcrest
import pytest
import yaml
import allure
import pytest_dependency

from pages.app import BaseTest

'''
新增列管 pass
'''
@allure.feature('管理')
class TestAddManagement:
    def setup(self):
        self.app = BaseTest()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.close()


    @allure.story("新增管理")
    @pytest.mark.parametrize(['username','passwd','user_idcard','reason','management_reason','measures','address','phone','assert_content'],
                             yaml.safe_load(open("./datas/data.yml",encoding='utf-8'))['add_management'])
    def test_add(self,username,passwd,user_idcard,reason,management_reason,measures,address,phone,assert_content):
        title = self.main.login(f"{username}",f"{passwd}").goto_in_manage().search(f"{user_idcard}").add_management()\
            .source().demand().level().member_type().member_label().group().reason(f"{reason}").management_reason(f"{management_reason}")\
            .control_measures(f"{measures}").live_address(f"{address}").phone(f"{phone}").status().stability_status()\
            .select_leader().submit().get_title()
        hamcrest.assert_that(title,hamcrest.contains_string(f"{assert_content}"))


    @allure.story('所长审批')
    @pytest.mark.dependency(name='test_add')
    @pytest.mark.parametrize(["username","passwd","comments","assert_content"],
                             yaml.safe_load(open("./datas/data.yml",encoding='utf-8'))['add_approve_1'])
    def test_approve_agree(self,username,passwd,comments,assert_content):
        result = self.main.login(f"{username}",f"{passwd}").goto_unchecked().goto_approve_detail().select_leader()\
            .input_comments(f"{comments}").click_complete().get_toast()
        hamcrest.assert_that(result,hamcrest.contains_string(f"{assert_content}"))


    @allure.story('局长审批')
    @pytest.mark.dependency(name='test_add')
    @pytest.mark.parametrize(["username","passwd","comments","assert_content"],
                             yaml.safe_load(open("./datas/data.yml",encoding='utf-8'))['add_approve_2'])

    def test_approve_disagree(self,username,passwd,comments,assert_content):
        result = self.main.login(f"{username}",f"{passwd}").goto_unchecked().goto_approve_detail().input_comments(f"{comments}")\
        .click_complete().get_toast()
        hamcrest.assert_that(result,hamcrest.contains_string(f"{assert_content}"))