import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestVip:
    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("vip_data.yaml","test_vip"))
    def test_vip(self,args):
        code = args["code"]
        expect = args["expect"]
        self.page.home.login_is_not(self.page)
        self.page.me.click_be_vip_btn()
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        self.page.vip.input_invite_code(code)
        self.page.vip.click_invite_vip_btn()
        assert self.page.vip.is_keyword_in_page_source(expect)
        self.driver.switch_to.context("NATIVE_APP")

