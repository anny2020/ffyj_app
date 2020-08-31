from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base
from pages.groupwarningdetail_page import GroupWarningDetailPage
from pages.my_page import MyPage
from pages.notice_page import NoticePage
from pages.person_list_page import PersonListPage
from pages.statistics_page import StatisticsPage
from pages.unchecked_page import UncheckedPage
from pages.unvisited_page import UnvisitedPage
from pages.warning_detail_page import WarningDetailPage
from pages.warninglist_page import WarningListPage
'''
主页
'''

class MainPage(Base):

    _ele_notice = (MobileBy.ID,"com.hnhy.petition:id/iv_function_left")
    _ele_groupwarning = (MobileBy.XPATH,'//*[@text="群体预警"]')
    _ele_warning = (MobileBy.XPATH,'//*[contains(@text,"预警")]')
    _ele_unvisited = (MobileBy.XPATH,'//*[@text="待走访"]')
    _ele_unchecked = (MobileBy.XPATH, '//*[@text="待审核"]')
    _ele_worktarget = (MobileBy.XPATH, '//*[@text="工作对象"]')
    _ele_archive = (MobileBy.XPATH, '//*[@text="人员档案"]')
    _ele_check = (MobileBy.XPATH, '//*[@text="人员核查"]')
    _ele_StabilityControl = (MobileBy.XPATH, '//*[@text="稳控工作"]')
    _ele_in_manage = (MobileBy.XPATH, '//*[@text="列管管理"]')
    _ele_out_manage = (MobileBy.XPATH, '//*[@text="撤管管理"]')
    _ele_strike = (MobileBy.XPATH, '//*[@text="打击处理"]')
    _ele_transfer = (MobileBy.XPATH, '//*[@text="人员移交"]')
    _ele_check_report = (MobileBy.XPATH, '//*[@text="盘查上报"]')
    _ele_registration = (MobileBy.XPATH, '//*[@text="上访登记"]')
    _ele_main = (MobileBy.XPATH, '//*[@text="首页"]')
    _ele_warning = (MobileBy.XPATH,'//*[@text="预警"]')
    _ele_statistics = (MobileBy.XPATH,'//*[@text="统计"]')
    _ele_my = (MobileBy.XPATH,'//*[@text="我的"]')


    # 通知公告
    def goto_notices(self):
        self.find_and_click(self._ele_notice)
        return NoticePage(self.driver)

    #群体事件预警详情 由管理员帐号来处理此功能
    def goto_groupwarning_detail(self):
        elements = self.find_elements(self._ele_groupwarning)
        #点击最上面的一个
        elements[-1].click()
        return GroupWarningDetailPage(self.driver)

    #一般预警 由警员处理
    def goto_warning_detail(self):
        elements = self.find_elements(self._ele_warning)
        elements[-1].click()
        return WarningDetailPage(self.driver)


    #待走访
    def goto_unvisited(self):
        self.find_and_click(self._ele_unvisited)
        return UnvisitedPage(self.driver)

    #待审核
    def goto_unchecked(self):
        self.find_and_click(self._ele_unchecked)
        return UncheckedPage(self.driver)


    #工作对象
    def goto_worktarget(self):
        self.find_and_click(self._ele_worktarget)
        return PersonListPage(self.driver)


    #人员档案
    def goto_archive(self):
        self.find_and_click(self._ele_archive)
        return PersonListPage(self.driver)


    #人员核查
    def goto_check(self):
        self.find_and_click(self._ele_check)
        return PersonListPage(self.driver)


    #稳控工作
    def goto_StabilityControl(self):
        self.find_and_click(self._ele_StabilityControl)
        return PersonListPage(self.driver)


    #列管管理
    def goto_in_manage(self):
        self.find_and_click(self._ele_in_manage)
        return PersonListPage(self.driver)

    #撤管管理
    def goto_out_manage(self):
        self.find_and_click(self._ele_out_manage)
        return PersonListPage(self.driver)

    #打击处理
    def goto_strike(self):
        self.find_and_click(self._ele_strike)
        return PersonListPage(self.driver)

    #人员移交
    def goto_transfer(self):
        self.find_and_click(self._ele_transfer)
        return PersonListPage(self.driver)

    #盘查上报
    def goto_check_report(self):
        self.find_and_click(self._ele_check_report)
        return PersonListPage(self.driver)

    #上访登记
    def goto_registration(self):
        self.find_and_click(self._ele_registration)
        return PersonListPage(self.driver)

    #首页
    def goto_my(self):
        self.find_and_click(self._ele_main)
        return MyPage(self.driver)

    #预警
    def goto_warninglist(self):
        self.find_and_click(self._ele_warning)
        return WarningListPage(self.driver)

    #统计
    def goto_statistics(self):
        self.find_and_click(self._ele_statistics)
        return StatisticsPage(self.driver)

    #我的
    def goto_my(self):
        self.find_and_click(self._ele_my)
        return MyPage(self.driver)


