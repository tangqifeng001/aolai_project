import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver(False)
        self.page = Page()
    def teardown(self):
        time.sleep(5)
        self.driver.quit()
    # def test_login_if_not(self):
    #     self.page.home.login_is_not(self.page)

    @pytest.mark.parametrize("args",analyze_file("login_data.yaml","test_login"))
    def test_login(self,args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        self.page.home.click_me()
        self.page.register.click_register()
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_login_btn()

        # 断言
        if toast is None:
            assert self.page.me.get_nick_name_text_view() == username
        else:
            assert self.page.login.is_toast_exist(toast)

