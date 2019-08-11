import allure
import time
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class VipPage(BasePage):
    invite_code = By.XPATH, "//*[@type='tel']"
    invite_vip_btn = By.XPATH,"//*[@value='立即成为会员']"

    @allure.step(title='输入邀请码')
    def input_invite_code(self,code):
        self.input(self.invite_code,code)

    @allure.step(title='点击立即成为会员')
    def click_invite_vip_btn(self):
        self.click(self.invite_vip_btn)

