import time

from base.base_driver import init_driver
from page.page import Page


class TestUpdate:
    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(5)
        self.driver.quit()
    def test_update(self):
        self.page.home.login_is_not(self.page)
        time.sleep(3)
        self.page.me.click_setting_btn()
        self.page.setting.click_about_aolai_btn()
        self.page.about.click_update()
        assert self.page.about.is_toast_exist("当前已是最新版本")