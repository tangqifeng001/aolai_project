from base.base_driver import init_driver
from page.page import Page


class TestUpdate:
    def setup(self):
        self.driver = init_driver(True)
        self.page = Page()
    def test_update(self):
        self.page.home.login_is_not(self.page)
        self.page.me.click_setting_btn()
        self.page.setting.click_about_aolai_btn()
        self.page.about.click_update()
        assert self.page.about.is_toast_exist("当前已是最新版本")