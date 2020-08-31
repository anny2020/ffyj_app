from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base


class StrikePage(Base):
    _ele_select = (MobileBy.XPATH,'//*[@text="请选择"]')
    _ele_select_value = (MobileBy.XPATH,'//*[@text="训诫"]')
    _ele_reason = (MobileBy.XPATH,'//*[contains(@text,"请填写处理原因")]')
    _ele_comments = (MobileBy.XPATH,'//*[contains(@text,"请填写备注信息")]')
    _ele_image = (MobileBy.ID,'com.hnhy.petition:id/img')
    _ele_shutter_button = (MobileBy.ACCESSIBILITY_ID,'快门')
    _ele_save_image = (MobileBy.ACCESSIBILITY_ID,'完成')
    _ele_submit = (MobileBy.XPATH,'//*[@text="提交"]')
    _ele_toast = (MobileBy.XPATH,'//*[@class="android.widget.Toast"]')


    def type(self):
        self.find_and_click(self._ele_select)
        self.find_and_click(self._ele_select_value)
        return self

    def reason(self,reason):
        self.find_and_sendkeys(self._ele_reason,reason)
        return self

    def remarks(self,remarks):
        self.find_and_sendkeys(self._ele_comments,remarks)
        return self

    def photo(self):
        self.find_and_click(self._ele_image)
        self.find_and_click(self._ele_shutter_button)
        self.find_and_click(self._ele_save_image)
        return self

    def submit(self):
        self.find_and_click(self._ele_submit)
        from pages.member_detail_page import MemberDetailPage
        return MemberDetailPage(self.driver)

