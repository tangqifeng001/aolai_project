import time
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
        print(good_title)
        self.page.good_detail.click_add_shop_cart_btn()
        self.page.good_detail.click_spec()
        self.page.good_detail.click_shop_cart()
        time.sleep(2)
        # 断言
        assert self.page.good_detail.is_keyword_in_page_source(good_title)
