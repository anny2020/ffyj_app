from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base
from pages.member_detail_page import MemberDetailPage


class PersonListPage(Base):
    _ele_search_input = (MobileBy.XPATH, '//*[contains(@text,"输入")]')
    _ele_search_btn = (MobileBy.ID, 'com.hnhy.petition:id/btn_search')
    _ele_member = (MobileBy.ID,'com.hnhy.petition:id/id_card')
    _ele_text_views = (MobileBy.XPATH, '//*[@class="android.widget.TextView"]')


    def search(self,user_idcard):
        self.find_and_sendkeys(self._ele_search_input,user_idcard)
        self.find_and_click(self._ele_search_btn)
        self.find_and_click(self._ele_member)
        return MemberDetailPage(self.driver)

#对于无return页面的search
    def search_2(self,user_idcard):
        self.find_and_sendkeys(self._ele_search_input, user_idcard)
        self.find_and_click(self._ele_search_btn)
        text_views = self.find_elements(self._ele_text_views)
        j = []
        for text_view in text_views:
            j.append(text_view.text)
        if user_idcard in j:
            return True
        else:
            return False

