import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class SettingPage(BasePage):
    about_aolai_btn = By.XPATH,"//*[@text='关于百年奥莱']"
    @allure.step(title='点击百年奥莱')
    def click_about_aolai_btn(self):
        self.find_element_with_scroll(self.about_aolai_btn).click()