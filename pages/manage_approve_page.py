from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base
'''
列管审批页面
'''

class ManageApprovePage(Base):
    _ele_leader = (MobileBy.XPATH,'//*[@text="责任局长:"]/../android.widget.LinearLayout')
    _ele_selector = (MobileBy.XPATH,'//*[contains(@text,"局长")]/../android.widget.ImageView')
    _ele_disagree = (MobileBy.XPATH,'//*[@text="不同意"]')
    _ele_approval_comments = (MobileBy.XPATH,'//*[contains(@text,"请填写审批意见")]')
    _ele_complete = (MobileBy.XPATH,'//*[@text="完成"]')
    _ele_toast = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
    #用于判断审批角色的元素
    _ele_approve_result = (MobileBy.XPATH,'//*[@text="审批结果:"]')

    #选择责任
    def select_leader(self):
        self.find_and_click(self._ele_leader)
        self.find_and_click(self._ele_selector)
        return self

    def click_disagree(self):
        self.find_and_click(self._ele_disagree)
        return self

    def input_comments(self,comments):
        self.find_and_sendkeys(self._ele_approval_comments,comments)
        return self

    def click_complete(self):
        if not self.is_displayed(self._ele_complete):
            self.slipe()
        self.find_and_click(self._ele_complete)
        from pages.unchecked_page import UncheckedPage
        return UncheckedPage(self.driver)

    def get_toast(self):
        toast = self.get_toast()
        return toast
