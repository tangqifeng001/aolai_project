import random

import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class CategoryPage(BasePage):
    goods_list_btn = By.ID,"com.yunmall.lc:id/iv_img"
    @allure.step(title='分类 点击进入商品列表')
    def click_goods_list(self):
        goods_list = self.find_elements(self.goods_list_btn)
        goods_list_count = len(goods_list)
        goods_list[random.randint(0,goods_list_count-1)].click()
