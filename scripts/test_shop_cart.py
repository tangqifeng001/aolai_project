import time

from selenium.webdriver.common.by import By

from base.base_driver import init_driver
from page.page import Page


class TestAddShopCart:
    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_add_shop_cart(self):
        self.page.home.login_is_not(self.page)
        self.page.home.click_category_btn()
        self.page.category.click_goods_list()
        self.page.goods_list.click_goods()
        good_title = self.page.good_detail.get_good_title_text()
        self.page.good_detail.click_add_shop_cart_btn()
        self.page.good_detail.click_spec()
        self.page.good_detail.click_shop_cart()
        time.sleep(2)
        # 断言
        xpath_feature = By.XPATH,"//*[contains(@text,'%s')]" % good_title
        assert self.page.good_detail.is_feature_exist(xpath_feature)
        # assert self.page.good_detail.is_keyword_in_page_source(good_title)
    def test_cart_price(self):
        self.page.home.login_is_not(self.page)
        time.sleep(3)
        self.page.home.click_shop_cart_btn()
        if self.page.shop_cart.is_cart_empty():
            self.page.home.click_category_btn()
            self.page.category.click_goods_list()
            self.page.goods_list.click_goods()
            self.page.good_detail.click_add_shop_cart_btn()
            self.page.good_detail.click_spec()
            self.page.good_detail.press_back()
            time.sleep(2)
            self.page.goods_list.press_back()
            self.page.home.click_shop_cart_btn()
        self.page.shop_cart.click_select_all()
        all_price = self.page.shop_cart.get_count_price()
        self.page.shop_cart.click_edit_btn()
        self.page.shop_cart.click_add()
        self.page.shop_cart.click_finish()
        assert self.page.shop_cart.get_count_price() == all_price + self.page.shop_cart.get_price()
    def test_clear_shop_cart(self):
        self.page.home.login_is_not(self.page)
        time.sleep(3)
        self.page.home.click_shop_cart_btn()
        if self.page.shop_cart.is_cart_empty():
            self.page.home.click_category_btn()
            self.page.category.click_goods_list()
            self.page.goods_list.click_goods()
            self.page.good_detail.click_add_shop_cart_btn()
            self.page.good_detail.click_spec()
            self.page.good_detail.press_back()
            time.sleep(2)
            self.page.goods_list.press_back()
            self.page.home.click_shop_cart_btn()
        self.page.shop_cart.click_select_all()
        self.page.shop_cart.click_edit_btn()
        self.page.shop_cart.click_delete()
        self.page.shop_cart.click_right()
        assert self.page.shop_cart.is_cart_empty()