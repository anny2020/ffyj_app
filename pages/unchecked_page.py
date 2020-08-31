from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base

#待审核页面
from pages.manage_approve_page import ManageApprovePage


class UncheckedPage(Base):
    _ele_member = (MobileBy.XPATH,'//*[@text="周一"]')

    def goto_approve_detail(self):
        self.find_and_click(self._ele_member)
        return ManageApprovePage(self.driver)