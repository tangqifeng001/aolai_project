import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class HomePage(BasePage):
    me_btn = By.ID, "com.yunmall.lc:id/tab_me"
    category_btn = By.ID,"com.yunmall.lc:id/tab_category"
    shop_cart_btn = By.ID, "com.yunmall.lc:id/tab_shopping_cart"
    search_btn = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
    home_btn = By.ID,"com.yunmall.lc:id/tab_home"
    # 点击 我
    @allure.step(title='首页 点击我')
    def click_me(self):
        self.click(self.me_btn)

    @allure.step(title='首页 点击放大镜')
    def click_search_btn(self):
        self.click(self.search_btn)

    @allure.step(title='首页 点击首页')
    def click_home_btn(self):
        self.click(self.home_btn)

    @allure.step(title='首页 如果没登录，点击去登录')
    def login_is_not(self,page):
        # 判断登录状态
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        # 没有登录就去登录
        # 点击 已有账号
        page.register.click_register()
        # 输入用户名
        page.login.input_username("tangqifeng")
        # 输入密码
        page.login.input_password("123456")
        # 点击登录
        page.login.click_login_btn()

    @allure.step(title='首页 点击分类按钮')
    def click_category_btn(self):
        self.click(self.category_btn)

    @allure.step(title='首页 点击分类按钮')
    def click_category_btn(self):
        self.click(self.category_btn)

    @allure.step(title='首页 点击购物车按钮')
    def click_shop_cart_btn(self):
        self.click(self.shop_cart_btn)
