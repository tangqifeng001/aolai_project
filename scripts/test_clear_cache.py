from base.base_driver import init_driver
from page.page import Page


class TestClearCache:
    def setup(self):
        self.driver = init_driver(False)
        self.page = Page()
    def test_clear_cache(self):
        self.page.home.login_is_not(self.page)
        self.page.me.click_setting_btn()
        self.page.setting.click_clear_cache_btn()

        assert self.page.about.is_toast_exist("清理成功")