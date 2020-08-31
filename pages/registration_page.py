from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base


class RegistrationPage(Base):
    _ele_petition_type = (MobileBy.XPATH,'//*[@text="上访类型:"]/../android.widget.TextView[2]')
    _ele_petition_value =(MobileBy.XPATH,'//*[@text="进京访"]')
    _ele_repatriate_date = (MobileBy.XPATH,'//*[@text="选择遣返时间(可不选)"]')
    _ele_confirm = (MobileBy.XPATH,'//*[@text="确定"]')
    _ele_live_status = (MobileBy.XPATH,'//*[@text="居住状态:"]/../android.widget.TextView[2]')
    _ele_live_value = (MobileBy.XPATH,'//*[@text="户籍地居住"]')
    _ele_demands = (MobileBy.XPATH,'//*[contains(@text,"请填写涉访诉求")]')
    _ele_submit = (MobileBy.XPATH,'//*[@text="提交"]')
    _ele_toast = (MobileBy.XPATH,'//*[@class="android.widget.Toast"]')


    def type(self):
        self.find_and_click(self._ele_petition_type)
        self.find_and_click(self._ele_petition_value)
        return self

    def date(self):
        self.find_and_click(self._ele_repatriate_date)
        self.find_and_click(self._ele_confirm)
        return self

    def live_status(self):
        self.find_and_click(self._ele_live_status)
        self.find_and_click(self._ele_live_value)
        return self

    def demands(self,demands):
        self.find_and_sendkeys(self._ele_demands,demands)
        return self

    def submit(self):
        self.find_and_click(self._ele_submit)
        from pages.member_detail_page import MemberDetailPage
        return MemberDetailPage(self.driver)








