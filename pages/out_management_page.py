from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base

'''
撤管页面-OK
'''
class OutManagementPage(Base):
    _ele_reason= (MobileBy.XPATH,'//*[@text="请选择"]')
    _ele_reason_value = (MobileBy.XPATH,'//*[@text="息访"]')
    _ele_comments = (MobileBy.XPATH,'//*[@text="请填写说明信息"]')
    _ele_submit = (MobileBy.XPATH,'//*[@text="提交"]')
    _ele_toast = (MobileBy.XPATH,'//*[@class="android.widget.Toast"]')

    #原因
    def select_reason(self):
        self.find_and_click(self._ele_reason)
        self.find_and_click(self._ele_reason_value)
        return self

    #说明
    def input_comments(self,reason):
        self.find_and_sendkeys(self._ele_comments,reason)
        return self

    #提交
    def click_submit(self):
        self.find_and_click(self._ele_submit)
        from pages.member_detail_page import MemberDetailPage
        return MemberDetailPage(self.driver)


    def get_toast(self):
        toast = self.get_toast()




