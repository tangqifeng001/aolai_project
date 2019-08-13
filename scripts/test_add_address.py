import time

from base.base_driver import init_driver
from page.page import Page


class TestAddAddress:
    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(5)
        self.driver.quit()
    def test_add_address(self):
        self.page.home.login_is_not(self.page)
        self.page.me.click_setting_btn()
        self.page.setting.click_address_list()
        self.page.address_list.click_add_address()
        self.page.edit_address.input_receipt_name("李三")
        self.page.edit_address.input_add_phone("18888888888")
        self.page.edit_address.input_addr_info("三单元 403")
        self.page.edit_address.input_post_code("262300")
        self.page.edit_address.click_address_default()
        self.page.edit_address.choose_region()
        self.page.edit_address.click_save_btn()
        assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % ("李三","18888888888")