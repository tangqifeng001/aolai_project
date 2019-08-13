import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestAddAddress:
    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(5)
        self.driver.quit()
    @pytest.mark.parametrize("args",analyze_file("address_data.yaml","test_add_address"))
    def test_add_address(self,args):
        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        post_code = args["post_code"]
        toast = args["toast"]
        self.page.home.login_is_not(self.page)
        self.page.me.click_setting_btn()
        self.page.setting.click_address_list()
        self.page.address_list.click_add_address()
        self.page.edit_address.input_receipt_name(name)
        self.page.edit_address.input_add_phone(phone)
        self.page.edit_address.input_addr_info(info)
        self.page.edit_address.input_post_code(post_code)
        self.page.edit_address.click_address_default()
        self.page.edit_address.choose_region()
        self.page.edit_address.click_save_btn()
        if toast is None:
            assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % (name,phone)
        else:
            assert self.page.edit_address.is_toast_exist(toast)