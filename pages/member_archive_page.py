from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base


class MemberArchivePage(Base):
    _ele_memeber_name = (MobileBy.XPATH,'//*[@text="姓名:"]/../android.widget.TextView[2]')
    _ele_member_idcard = (MobileBy.XPATH,'//*[@text="身份证号:"]/../android.widget.TextView[2]')

    def get_member_info(self):

        memname = self.find_element(self._ele_memeber_name).text
        memidcard = self.find_element(self._ele_member_idcard).text
        return memname,memidcard

