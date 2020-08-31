from appium.webdriver.common.mobileby import MobileBy

from pages.approve_result_detail_page import ApproveResultDetail
from pages.base_page import Base



class NoticePage(Base):

    _ele_all = (MobileBy.XPATH,"//*[@text='全部']")
    _ele_haveread = (MobileBy.XPATH,"//*[@text='已读']")
    _ele_unread = (MobileBy.XPATH,"//*[@text='未读']")
    _ele_approveresult = (MobileBy.XPATH,"//*[@text='审批结果']")
    _ele_leftarrow = (MobileBy.ID,"com.hnhy.petition:id/iv_function_left")
    _ele_remove = (MobileBy.ID,"com.hnhy.petition:id/rl_function_right")
    _ele_select_btn = (MobileBy.ID,"com.hnhy.petition:id/btn_select")
    _ele_delete_btn = (MobileBy.XPATH,'//*[@text="删除"]')
    _ele_toast = (MobileBy.XPATH,'//*[@class="android.widget.Toast"]')


    def all(self):
        self.find_and_click(self._ele_all)
        return self


    def have_read(self):
        self.find_and_click(self._ele_haveread)
        return self


    def unread(self):
        self.find_and_click(self._ele_unread)
        return self


    def back(self):
        self.find_and_click(self._ele_leftarrow)
        from pages.main_page import MainPage
        return MainPage(self.driver)

    def remove_icon(self):
        self.find_and_click(self._ele_remove)
        return self

    def select_remove(self):
        self.find_and_click(self._ele_select_btn)
        return self

    def delete_btn(self):
        self.find_and_click(self._ele_delete_btn)
        return self




