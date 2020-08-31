from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base


'''
新增稳控工作页
'''
class StabilityControlDetailPage(Base):
    # 稳控类型
    _ele_stability_type = (MobileBy.ID,'com.hnhy.petition:id/tv_control_type')
    #稳控状态
    _ele_stability_status = (MobileBy.ID,'com.hnhy.petition:id/tv_control_status')

    # 稳控类型选项
    _ele_daily = (MobileBy.XPATH,'//*[@text="日常稳控"]/../android.widget.ImageView')
    _ele_sensitive = (MobileBy.XPATH,'//*[@text="敏感时期稳控"]/../android.widget.ImageView')
    # 稳控状态类型
    _ele_undercontrol = (MobileBy.XPATH,'//*[@text="在控"]/../android.widget.ImageView')
    _ele_outofcontrol = (MobileBy.XPATH,'//*[@text="失控"]/../android.widget.ImageView')
    # 稳控地点
    _ele_place = (MobileBy.XPATH,'//*[contains(@text,"请输入稳控地点")]')
    # 稳控描述
    _ele_describe = (MobileBy.XPATH,'//*[contains(@text,"请填写稳控描述")]')
    # 涉访人表现
    _ele_behaviour = (MobileBy.XPATH,'//*[contains(@text,"请填写涉访人表现")]')
    # 备注
    _ele_remarks = (MobileBy.XPATH,'//*[contains(@text,"请填写备注")]')
    # 提交
    _ele_submit = (MobileBy.XPATH,'//*[contains(@text,"提交")]')

    _ele_toast = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')


    def type(self):
        self.find_and_click(self._ele_stability_type)
        self.find_and_click(self._ele_daily)
        return self

    def status(self):
        self.find_and_click(self._ele_stability_status)
        self.find_and_click(self._ele_undercontrol)
        return self

    def place(self,place):
        self.find_and_sendkeys(self._ele_place,place)
        return self

    def describe(self,describe):
        self.find_and_sendkeys(self._ele_describe,describe)
        return self

    def behaviour(self,behaviour):
        self.find_and_sendkeys(self._ele_behaviour,behaviour)
        return self

    def remarks(self,remarks):
        self.find_and_sendkeys(self._ele_remarks,remarks)
        return self

    def submit(self):
        self.find_and_click(self._ele_submit)
        from pages.member_detail_page import MemberDetailPage
        return MemberDetailPage(self.driver)
