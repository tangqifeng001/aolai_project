import time

from base.base_driver import init_driver
from page.page import Page


class TestClearCache:
    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(5)
        self.driver.quit()
    def test_clear_cache(self):
        self.page.home.login_is_not(self.page)
        time.sleep(3)
        self.page.me.click_setting_btn()
        self.page.setting.click_clear_cache_btn()

        assert self.page.about.is_toast_exist("清理成功")