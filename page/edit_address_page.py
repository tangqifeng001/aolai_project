import random

import allure
import time
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class EditAddressPage(BasePage):
    receipt_name = By.ID,"com.yunmall.lc:id/address_receipt_name"
    add_phone = By.ID,"com.yunmall.lc:id/address_add_phone"
    addr_info = By.ID,"com.yunmall.lc:id/address_detail_addr_info"
    post_code = By.ID,"com.yunmall.lc:id/address_post_code"
    address_default = By.ID,"com.yunmall.lc:id/address_default"
    address_region = By.ID,"com.yunmall.lc:id/address_province"
    save_btn = By.ID,"com.yunmall.lc:id/button_send"
    @allure.step(title='输入收件人')
    def input_receipt_name(self,name):
        self.input(self.receipt_name,name)

    @allure.step(title='输入手机号')
    def input_add_phone(self, phone):
        self.input(self.add_phone, phone)

    @allure.step(title='输入详细地址')
    def input_addr_info(self, info):
        self.input(self.addr_info, info)

    @allure.step(title='输入邮编')
    def input_post_code(self, code):
        self.input(self.post_code, code)

    @allure.step(title='点击设为默认地址')
    def click_address_default(self):
        self.click(self.address_default)

    @allure.step(title='点击保存')
    def click_save_btn(self):
        self.click(self.save_btn)

    @allure.step(title='点击所在地区')
    def click_address_region(self):
        self.click(self.address_region)

    @allure.step(title='选择省市区')
    def choose_region(self):
        self.click_address_region()
        time.sleep(1)
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            areas = self.find_elements((By.ID,"com.yunmall.lc:id/area_title"))
            areas_count = len(areas)
            areas[random.randint(0,areas_count - 1)].click()
            time.sleep(1)
