import time
import pytest
from selenium.webdriver.common.by import By

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestSearch:
    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(5)
        self.driver.quit()
    @pytest.mark.parametrize("args",analyze_file("search_data.yaml","test_search"))
    def test_search(self,args):
        kwd = args["keyword"]
        self.page.home.login_is_not(self.page)
        time.sleep(5)
        self.page.home.click_home_btn()
        self.page.home.click_search_btn()
        self.page.search.input_search_kwd(kwd)
        self.page.search.click_search_btn()
        time.sleep(5)
        self.page.search.press_back()
        # 断言
        xpath_feature = By.XPATH,"//*[@resource-id='com.yunmall.lc:id/keyayout']/*/*[@text='%s']" % kwd
        assert self.page.search.is_feature_exist(xpath_feature)
    def test_del_search_text(self):
        self.page.home.login_is_not(self.page)
        time.sleep(5)
        self.page.home.click_home_btn()
        self.page.home.click_search_btn()
        self.page.search.input_search_kwd("面膜")
        self.page.search.click_search_btn()
        time.sleep(3)
        self.page.search.press_back()
        self.page.search.click_search_del()
        # 断言
        xpath_feature = By.XPATH,"//*[@text='暂无搜索历史']"
        assert self.page.search.is_feature_exist(xpath_feature)