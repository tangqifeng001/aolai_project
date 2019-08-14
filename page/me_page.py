import allure
import time
from selenium.webdriver.common.by import By

from base.base_action import BasePage


class MePage(BasePage):
    nick_name_text_view = By.ID,"com.yunmall.lc:id/tv_user_nikename"
    setting_btn = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
    be_vip_btn = By.ID,"com.yunmall.lc:id/tv_my_shop_text"
    # 获取我的页面
    @allure.step(title='我的页 获取登录昵称')
    def get_nick_name_text_view(self):
        return self.get_element_text(self.nick_name_text_view)

    @allure.step(title='我的页 点击设置按钮')
    def click_setting_btn(self):
        self.click(self.setting_btn)

    @allure.step(title='我的页 点击加入超级VIP')
    def click_be_vip_btn(self):
        self.find_element_with_scroll(self.be_vip_btn).click()
        time.sleep(10)
