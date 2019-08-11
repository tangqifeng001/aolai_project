from selenium.webdriver.common.by import By

from base.base_action import BasePage


class LoginPage(BasePage):
    username = By.ID,"com.yunmall.lc:id/logon_account_textview"
    password = By.ID,"com.yunmall.lc:id/logon_password_textview"
    login_btn = By.ID,"com.yunmall.lc:id/logon_button"
    # 输入用户名
    def input_username(self,username):
        self.input(self.username,username)

    # 输入密码
    def input_password(self,pwd):
        self.input(self.password,pwd)

    # 点击登录
    def click_login_btn(self):
        self.click(self.login_btn)