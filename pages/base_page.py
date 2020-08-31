from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait



class Base:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find_element(self,locator):
        return self.driver.find_element(*locator)

    def find_elements(self,locator):
        return self.driver.find_elements(*locator)


    def find_and_click(self,locator):
        return self.driver.find_element(*locator).click()


    def find_and_sendkeys(self,locator,value):
        return self.driver.find_element(*locator).send_keys(value)



    def find_by_scroll(self,text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).'
                                   f'instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));').click()

    def find_and_wait(self,text):
        return WebDriverWait(self.driver,15).until_not(lambda x:x.find_element_by_xpath(f"//*[@text='{text}']"))

    def back(self,num=1):
        for i in range(num):
            self.driver.back()

    # def is_displayed(self,locator):
    #     try:
    #         if self.find_element(locator).is_displayed():
    #             return True
    #     except NoSuchContextException:
    #         return False


    def slipe(self):
        action = TouchAction(self.driver)
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        x1 = int(width/2)
        y_start = int(height*0.8)
        y_end = int(height*0.2)
        action.press(x=x1,y=y_start).wait(100).move_to(x=x1,y=y_end).wait(100).release().perform()

    def get_toast(self):
        self._ele_member = (MobileBy.XPATH,'//*[@class="android.widget.Toast"]')
        return self.find_element(self._ele_member).text