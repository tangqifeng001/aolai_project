import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class AddressListPage(BasePage):
    add_address_btn = By.XPATH,"//*[@text='新增地址']"
    default_receipt_name_text = By.ID,"com.yunmall.lc:id/receipt_name"
    @allure.step(title='点击新增地址')
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_btn).click()
    @allure.step(title='获取默认地址的姓名和电话')
    def get_default_receipt_name_text(self):
        return self.get_element_text(self.default_receipt_name_text)

