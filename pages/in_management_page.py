import time

from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import Base
'''
申请列管页面-OK
'''

class InManagementPage(Base):

    #新增列管表单字段
    _ele_source = (MobileBy.XPATH,'//*[@text="管控来源:"]/../android.widget.TextView[2]')
    #管控来源项
    _ele_public_security = (MobileBy.XPATH,'//*[@text="公安部交办"]/../android.widget.ImageView')
    _ele_provincial_department = (MobileBy.XPATH,'//*[@text="省厅交办"]/../android.widget.ImageView')
    _ele_work_find = (MobileBy.XPATH,'//*[@text="工作中发现"]/../android.widget.ImageView')
    #涉访诉求
    _ele_demand = (MobileBy.XPATH,'//*[@text="涉访诉求:"]/../android.widget.TextView[2]')
    #涉访诉求项
    _ele_civil_dispute = (MobileBy.XPATH,'//*[@text="民事纠纷类"]')
    _ele_family = (MobileBy.XPATH,'//*[@text="婚姻家庭"]/../android.widget.ImageView')
    #管控等级
    _ele_level = (MobileBy.XPATH,'//*[@text="管控等级:"]/../android.widget.TextView[2]')
    #A级
    _ele_levelA = (MobileBy.XPATH,'//*[@text="A级"]/../android.widget.ImageView')
    #人员类型
    _ele_member_type = (MobileBy.XPATH,'//*[@text="人员类型:"]/../android.widget.TextView[2]')
    #涉访人员
    _ele_interviewees = (MobileBy.XPATH,'//*[@text="涉访人员"]/../android.widget.ImageView')
    #人员标签
    _ele_member_label = (MobileBy.XPATH,'//*[@text="人员标签:"]/../android.widget.TextView[2]')

    #法轮功
    _ele_lable_name = (MobileBy.XPATH,'//*[@text="法轮功"]/../android.widget.ImageView')
    _ele_lable_confirm = (MobileBy.XPATH,'//*[@text="确定"]')
    #管辖单位
    _ele_jurisdiction_unit = (MobileBy.XPATH,'//*[@text="管辖单位:"]/../android.widget.TextView[2]')
    #河南省公安厅
    _ele_henan = (MobileBy.XPATH,'//*[contains(@text,"派出所")]/../android.widget.ImageView')
    #所属群体
    _ele_group = (MobileBy.XPATH,'//*[@text="所属群体:"]/../android.widget.TextView[2]')
    _ele_group_label = (MobileBy.XPATH, '//*[@text="讨薪"]/../android.widget.ImageView')
    _ele_group_lable_confirm = (MobileBy.XPATH,'//*[@text="确定"]')
    #填写涉访原因
    _ele_reason = (MobileBy.XPATH,'//*[contains(@text,"请填写涉访原因")]')
    #列管原因
    _ele_management_reason = (MobileBy.XPATH,'//*[contains(@text,"请填写列管原因")]')
    #管控措施
    _ele_control_measures = (MobileBy.XPATH,'//*[contains(@text,"请填写管控措施")]')
    #现在住址
    _ele_address = (MobileBy.XPATH,'//*[contains(@text,"请填写现有住址")]')
    #联系电话
    _ele_phone = (MobileBy.XPATH,'//*[contains(@text,"请填写联系电话")]')
    #当前状态
    _ele_status = (MobileBy.XPATH,'//*[@text="当前状态:"]/../android.widget.TextView[2]')
    #在家
    _ele_at_home = (MobileBy.XPATH,'//*[@text="在家"]/../android.widget.ImageView')
    # 稳控状态
    _ele_stability_status = (MobileBy.XPATH, '//*[@text="稳控状态:"]/../android.widget.TextView[2]')
    # 在家
    _ele_stability_value = (MobileBy.XPATH, '//*[@text="在控"]/../android.widget.ImageView')
    #责任所长
    _ele_director = (MobileBy.XPATH,'//*[@text="责任所长:"]/../android.widget.LinearLayout')
    _ele_director_value = (MobileBy.XPATH, '//*[contains(@text,"所长")]/../android.widget.ImageView')
    #提交
    _ele_submit = (MobileBy.XPATH,'//*[@text="提交"]')
    #获取不到toast,以回到人员详情页，获取人员详情标题做为判断条件
    _ele_header_title = (MobileBy.XPATH,'//*[@text="人员详情"]')


    def source(self):
        self.find_and_click(self._ele_source)
        self.find_and_click(self._ele_public_security)
        return self

    def demand(self):
        self.find_and_click(self._ele_demand)
        self.find_and_click(self._ele_civil_dispute)
        self.find_and_click(self._ele_family)
        return self

    def level(self):
        self.find_and_click(self._ele_level)
        self.find_and_click(self._ele_levelA)
        return self

    def member_type(self):
        self.find_and_click(self._ele_member_type)
        self.find_and_click(self._ele_interviewees)
        return self

    def member_label(self):
        self.find_and_click(self._ele_member_label)
        self.find_and_click(self._ele_lable_name)
        self.find_and_click(self._ele_lable_confirm)
        return self

    def group(self):
        self.find_and_click(self._ele_group)
        self.find_and_click(self._ele_group_label)
        self.find_and_click(self._ele_group_lable_confirm)
        return self

    def reason(self,reason):
        self.find_and_sendkeys(self._ele_reason,reason)
        return self

    def management_reason(self,management_reason):
        self.find_and_sendkeys(self._ele_management_reason,management_reason)
        return self


    def control_measures(self,measures):
        self.find_and_sendkeys(self._ele_control_measures,measures)
        return self

    def live_address(self,address):
        self.find_and_sendkeys(self._ele_address,address)
        return self

    def phone(self,phone):
        self.find_and_sendkeys(self._ele_phone,phone)
        return self

    def status(self):
        self.find_and_click(self._ele_status)
        self.find_and_click(self._ele_at_home)
        return self


    def stability_status(self):
        # if not self.is_displayed(self._ele_stability_status):
        self.slipe()
        time.sleep(5)
        self.find_and_click(self._ele_stability_status)
        self.find_and_click(self._ele_stability_value)
        return self

    def select_leader(self):
        self.find_and_click(self._ele_director)
        self.find_and_click(self._ele_director_value)
        return self


    def submit(self):
        self.find_and_click(self._ele_submit)
        from pages.member_detail_page import MemberDetailPage
        return MemberDetailPage(self.driver)



















