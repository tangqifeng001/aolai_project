import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class SettingPage(BasePage):
    about_aolai_btn = By.XPATH,"//*[@text='关于百年奥莱']"
    clear_cache_btn = By.ID,"com.yunmall.lc:id/setting_clear_cache"
    address_list_btn = By.XPATH,"//*[@text='地址管理']"
    @allure.step(title='点击百年奥莱')
    def click_about_aolai_btn(self):
        self.find_element_with_scroll(self.about_aolai_btn).click()

    @allure.step(title='点击清除缓存')
    def click_clear_cache_btn(self):
        self.find_element_with_scroll(self.clear_cache_btn).click()

    @allure.step(title='点击地址管理')
    def click_address_list(self):
        self.find_element_with_scroll(self.address_list_btn).click()