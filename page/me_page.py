import allure
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class MePage(BasePage):
    nick_name_text_view = By.ID,"com.yunmall.lc:id/tv_user_nikename"
    setting_btn = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
    # 获取我的页面
    @allure.step(title='获取登录昵称')
    def get_nick_name_text_view(self):
        return self.get_element_text(self.nick_name_text_view)

    @allure.step(title='点击设置按钮')
    def click_setting_btn(self):
        self.click(self.setting_btn)
