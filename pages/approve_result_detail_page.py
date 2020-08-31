from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base

'''
通知公告-审批结果详情页
'''
class ApproveResultDetail(Base):

    _ele_result = (MobileBy.ID,"com.hnhy.petition:id/tv_column_result")
    _ele_idcard = (MobileBy.ID,"com.hnhy.petition:id/id_card")

    def get_result(self):
        return self.find_element(self._ele_result).text,self.find_element(self._ele_idcard).text
