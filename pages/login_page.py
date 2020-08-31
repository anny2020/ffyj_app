from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base
from pages.main_page import MainPage


class LoginPage(Base):
    _ele_username = (MobileBy.ID,'com.hnhy.petition:id/username')
    _ele_passwd = (MobileBy.ID,'com.hnhy.petition:id/password')
    _ele_login = (MobileBy.XPATH,'//*[@text="登  录"]')

    def login(self,username,passwd):
        self.find_and_sendkeys(self._ele_username,username)
        self.find_and_sendkeys(self._ele_passwd,passwd)
        self.find_and_click(self._ele_login)
        return MainPage(self.driver)