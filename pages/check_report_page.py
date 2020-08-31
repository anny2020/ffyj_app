from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base


class CheckReportPage(Base):
    _ele_place = (MobileBy.XPATH,'//*[contains(@text,"请填写上报地点")]')
    _ele_detail_place = (MobileBy.XPATH,'//*[contains(@text,"请填写详细地址")]')
    _ele_disposal = (MobileBy.XPATH,'//*[@text="处置情况:"]/../android.widget.TextView[2]')
    _ele_disposal_value = (MobileBy.XPATH,'//*[contains(@text,"移交")]')
    _ele_describe = (MobileBy.XPATH,'//*[contains(@text,"请填写情况描述")]')
    _ele_submit = (MobileBy.XPATH,'//*[@text="提交"]')


    def place(self,place):
        self.find_and_sendkeys(self._ele_place,place)
        return self

    def detailed_place(self,detailed_place):
        self.find_and_sendkeys(self._ele_detail_place,detailed_place)
        return self

    def handle(self):
        self.find_and_click(self._ele_disposal)
        self.find_and_click(self._ele_disposal_value)
        return self

    def situation_described(self,described):
        self.find_and_sendkeys(self._ele_describe,described)
        return self

    def submit(self):
        self.find_and_click(self._ele_submit)
        from pages.member_detail_page import MemberDetailPage
        return MemberDetailPage(self.driver)

    # def get_toast(self):
    #     result = self.get_toast()
    #     return result





