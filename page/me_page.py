from selenium.webdriver.common.by import By

from base.base_action import BasePage


class MePage(BasePage):
    nick_name_text_view = By.ID,"com.yunmall.lc:id/tv_user_nikename"
    # 获取我的页面
    def get_nick_name_text_view(self):
        return self.get_element_text(self.nick_name_text_view)
