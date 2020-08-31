from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base
from pages.check_report_page import CheckReportPage
from pages.in_management_page import InManagementPage
from pages.member_transfer_page import MemberTransferPage
from pages.out_management_page import OutManagementPage
from pages.registration_page import RegistrationPage
from pages.stability_control_detail_page import StabilityControlDetailPage
from pages.strike_page import StrikePage

'''
人员详情页面
'''

class MemberDetailPage(Base):
    _ele_StabilityControl = (MobileBy.XPATH,'//*[@text="新增稳控工作"]')
    _ele_add_out_management = (MobileBy.XPATH,'//*[@text="新增撤管申请"]')
    _ele_add_management = (MobileBy.XPATH,'//*[@text="新增列管申请"]')
    _ele_add_strike = (MobileBy.XPATH,'//*[@text="新增打击处理"]')
    _ele_view_transfer_report = (MobileBy.XPATH,'//*[@text="查看移交报告"]')
    _ele_add_check_report = (MobileBy.XPATH,'//*[@text="新增盘查上报"]')
    _ele_add_registration = (MobileBy.XPATH,'//*[@text="新增上访登记"]')
    _ele_header_title = (MobileBy.XPATH,'//*[@text="人员详情"]')


    #新增稳控
    def add_StabilityControl(self):
        self.find_and_click(self._ele_StabilityControl)
        return StabilityControlDetailPage(self.driver)

    #列管
    def add_management(self):
        self.find_and_click(self._ele_add_management)
        return InManagementPage(self.driver)

    #撤管
    def add_out_management(self):
        self.find_and_click(self._ele_add_out_management)
        return OutManagementPage(self.driver)

    #打击处理
    def strike(self):
        self.find_and_click(self._ele_add_strike)
        return StrikePage(self.driver)

    #人员移交
    def view_transfer_report(self):
        self.find_and_click(self._ele_view_transfer_report)
        return MemberTransferPage(self.driver)

    #盘查上报
    def check_report(self):
        self.find_and_click(self._ele_add_check_report)
        return CheckReportPage(self.driver)

    #上访登记
    def registration(self):
        self.find_and_click(self._ele_add_registration)
        return RegistrationPage(self.driver)

    def get_title(self):
        return self.find_element(self._ele_header_title).text
