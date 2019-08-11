import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class HomePage(BasePage):
    me_btn = By.ID, "com.yunmall.lc:id/tab_me"
    # 点击 我
    @allure.step(title='点击我')
    def click_me(self):
        self.click(self.me_btn)

    @allure.step(title='如果没登录，点击去登录')
    def login_is_not(self,page):
        # 判断登录状态
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        # 没有登录就去登录
        # 点击 已有账号
        page.register.click_register()
        # 输入用户名
        page.login.input_username("itheima_test")
        # 输入密码
        page.login.input_password("itheima")
        # 点击登录
        page.login.click_login_btn()