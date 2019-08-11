import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class AboutPage(BasePage):
    update_btn = By.XPATH,"//*[@text='版本更新']"
    @allure.step(title='点击版本更新')
    def click_update(self):
        self.click(self.update_btn)