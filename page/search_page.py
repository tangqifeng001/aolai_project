import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class SearchPage(BasePage):
    search_kwd = By.ID, "com.yunmall.lc:id/text_search_keyword"
    search_btn = By.ID,"com.yunmall.lc:id/button_search"
    search_del = By.ID,"com.yunmall.lc:id/search_del"
    @allure.step(title='搜索页 输入搜索内容')
    def input_search_kwd(self,kwd):
        self.input(self.search_kwd,kwd)
    @allure.step(title='搜索页 点击搜索')
    def click_search_btn(self):
        self.click(self.search_btn)

    @allure.step(title='搜索页 点击删除')
    def click_search_del(self):
        self.click(self.search_del)

