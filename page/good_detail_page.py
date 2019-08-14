import allure
import time
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class GoodDetailPage(BasePage):
    add_shop_cart_btn = By.ID,"com.yunmall.lc:id/btn_add_to_shopping_cart"
    commit_btn = By.ID,"com.yunmall.lc:id/select_detail_sure_btn"
    good_title_text = By.ID,"com.yunmall.lc:id/tv_product_title"
    shop_cart_btn = By.ID, "com.yunmall.lc:id/btn_shopping_cart"
    @allure.step("商品详情页 点击加入购物车按钮")
    def click_add_shop_cart_btn(self):
        self.click(self.add_shop_cart_btn)
    @allure.step("商品详情页 点击确认按钮")
    def click_commit_btn(self):
        self.click(self.commit_btn)

    @allure.step("商品详情页 获取商品标题")
    def get_good_title_text(self):
        return self.get_element_text(self.good_title_text)
    @allure.step("商品详情页 点击购物车按钮")
    def click_shop_cart(self):
        self.click(self.shop_cart_btn)

    # 根据 "请选择 分类 规格" 获取 请选择后面的第一个规格的名字
    def get_choose_spec(self, text):
        print(text)
        print(text.split(" ")[1])
        return text.split(" ")[1]

    # 选择规格
    @allure.step(title='商品详情页 选择规格')
    def click_spec(self):
        while True:
            self.click_commit_btn()
            if self.is_toast_exist("请选择"):
                spec_name = self.get_choose_spec(self.get_toast_text("请选择"))
                spec_feature = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % spec_name
                self.click(spec_feature)
                time.sleep(6)
            else:
                break

