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
        time.sleep(3)
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
    def test_edit_address(self):
        self.page.home.login_is_not(self.page)
        time.sleep(5)
        self.page.me.click_setting_btn()
        self.page.setting.click_address_list()
        if not self.page.address_list.is_default_feature_exist():
            self.page.address_list.click_add_address()
            self.page.edit_address.input_receipt_name("tangqifeng")
            self.page.edit_address.input_add_phone("18888888888")
            self.page.edit_address.input_addr_info("三单元 876")
            self.page.edit_address.input_post_code("262300")
            self.page.edit_address.click_address_default()
            self.page.edit_address.choose_region()
            self.page.edit_address.click_save_btn()
        self.page.address_list.click_default_address()
        self.page.edit_address.input_receipt_name("zhaolixin")
        self.page.edit_address.input_add_phone("18888888888")
        self.page.edit_address.input_addr_info("三单元 876")
        self.page.edit_address.input_post_code("262300")
        self.page.edit_address.choose_region()
        self.page.edit_address.click_save_btn()
        assert self.page.edit_address.is_toast_exist("保存成功")
    def test_delete_address(self):
        self.page.home.login_is_not(self.page)
        time.sleep(3)
        self.page.me.click_setting_btn()
        self.page.setting.click_address_list()
        assert self.page.address_list.is_default_feature_exist(), "默认址不存在，没有地址可以删除"
        for i in range(10):
            self.page.address_list.click_edit_btn()
            if not self.page.address_list.is_delete_btn_exist():
                break
            self.page.address_list.click_delete_btn()
            self.page.address_list.click_commit_btn()
        self.page.address_list.click_edit_btn()
        assert not self.page.address_list.is_delete_btn_exist()


