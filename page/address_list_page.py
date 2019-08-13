import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class AddressListPage(BasePage):
    add_address_btn = By.XPATH,"//*[@text='新增地址']"
    default_receipt_name_text = By.ID,"com.yunmall.lc:id/receipt_name"
    default_address_btn = By.ID,"com.yunmall.lc:id/address_is_default"
    edit_btn = By.XPATH,"//*[@text='编辑']"
    delete_btn = By.XPATH,"//*[@text='删除']"
    commit_btn = By.XPATH,"//*[@text='确认']"
    @allure.step(title='点击新增地址')
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_btn).click()
    @allure.step(title='获取默认地址的姓名和电话')
    def get_default_receipt_name_text(self):
        return self.get_element_text(self.default_receipt_name_text)
    @allure.step(title='判断是否存在默认地址')
    def is_default_feature_exist(self):
        return self.is_feature_exist(self.default_receipt_name_text)
    @allure.step(title='点击默认地址')
    def click_default_address(self):
        self.click(self.default_address_btn)
    @allure.step(title='点击编辑')
    def click_edit_btn(self):
        self.click(self.edit_btn)
    @allure.step(title='点击删除')
    def click_delete_btn(self):
        self.click(self.delete_btn)
    @allure.step(title='点击确认')
    def click_commit_btn(self):
        self.click(self.commit_btn)

    @allure.step(title='判断是否存在删除')
    def is_delete_btn_exist(self):
        return self.is_feature_exist(self.delete_btn)





