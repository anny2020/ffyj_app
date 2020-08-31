from appium import webdriver

from pages.base_page import Base
from pages.login_page import LoginPage


class BaseTest(Base):

    #进行设备信息的初始化，并创建driver,这里放全局的信息，启动app
    def start(self):
        if self.driver is None:
            desired_caps = {
                'newCommandTimeout': "2000",
                "platformName": "Android",
                "platformVersion": "6.0.1",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.hnhy.petition",
                "appActivity": "com.hnhy.petition.mvp.ui.base.ActivityLoading",
                "noReset": True,
                "unicodeKeyBoard": True,
                "resetKeyBoard": True,
                "automationaName": "uiautomator2"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self


    def close(self):
        self.driver.close_app()

    #退出
    def quit(self):
        self.driver.quit()

    #回到首页

    def main(self):
        return LoginPage(self.driver)