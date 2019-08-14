import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class ShopCartPage(BasePage):
    edit_btn = By.XPATH,"//*[@text='编辑']"
    finish_btn = By.XPATH,"//*[@text='完成']"
    select_all_btn = By.ID,"com.yunmall.lc:id/iv_select_all"
    add_btn = By.ID,"com.yunmall.lc:id/iv_add"
    count_money = By.ID,"com.yunmall.lc:id/tv_count_money"
    price_feature = By.ID,"com.yunmall.lc:id/tv_price"
    delete_btn = By.ID, "com.yunmall.lc:id/tv_del_all"
    right_btn = By.ID,"com.yunmall.lc:id/ymdialog_right_button"
    @allure.step(title='购物车页面 点击编辑')
    def click_edit_btn(self):
        self.click(self.edit_btn)

    @allure.step(title='购物车页面 点击完成')
    def click_finish(self):
        self.click(self.finish_btn)

    @allure.step(title='购物车页面 点击全选')
    def click_select_all(self):
        self.click(self.select_all_btn)

    @allure.step(title='购物车页面 点击加号')
    def click_add(self):
        self.click(self.add_btn)

    @allure.step(title='购物车页面 点击删除')
    def click_delete(self):
        self.click(self.delete_btn)

    @allure.step(title='购物车页面 点击确认')
    def click_right(self):
        self.click(self.right_btn)
    @allure.step(title='购物车页面 处理价格')
    def deal_with_price(self,price):
        return float(price[2:])

    @allure.step(title='购物车页面 获取总价格')
    def get_count_price(self):
        count_price = self.get_element_text(self.count_money)
        return self.deal_with_price(count_price)
    @allure.step(title='购物车页面 获取单价')
    def get_price(self):
        price = self.get_element_text(self.price_feature)
        return self.deal_with_price(price)
    @allure.step(title="购物车页面 判断购物车是否为空")
    def is_cart_empty(self):
        xpath_feature = By.XPATH, "//*[contains(@text,'购物车还是空的')]"
        return self.is_feature_exist(xpath_feature)





