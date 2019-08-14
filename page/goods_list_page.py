import random

import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class GoodsListPage(BasePage):
    goods_btn = By.ID,"com.yunmall.lc:id/iv_element_1"
    @allure.step("商品列表页 点击一个商品")
    def click_goods(self):
        goods = self.find_elements(self.goods_btn)
        goods_count = len(goods)
        goods[random.randint(0,goods_count-1)].click()