import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class RegisterPage(BasePage):
    register_text_view = By.ID, "com.yunmall.lc:id/textView1"

    @allure.step(title='如果有账号，点击去登录')
    def click_register(self):
        self.click(self.register_text_view)
