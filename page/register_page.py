from selenium.webdriver.common.by import By

from base.base_action import BasePage


class RegisterPage(BasePage):
    register_text_view = By.ID, "com.yunmall.lc:id/textView1"
    def click_register(self):
        self.click(self.register_text_view)
