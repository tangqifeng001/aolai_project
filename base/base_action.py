# 封装定位一个元素的方法
# 封装定位多个元素的方法
# 定位元素，返回元素，需要传入特征feature,
# 设置显式等待，设置默认等待时间，频率。实际工作中，可以根据实际需要，修改等待时间
# 封装点击，输入，清空的操作
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver):
        self.driver = driver
    # 定位一个元素
    def find_element(self,feature,timeout=10,poll_frequency=1.0):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*feature))
    # 定位多个元素
    def find_elements(self,feature,timeout=10,poll_frequency=1.0):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_elements(*feature))
    # 点击操作
    def click(self,element):
        self.find_element(element).click()
    # 输入操作
    def input(self,element,content):
        self.find_element(element).send_keys(content)
    # 清空操作
    def clear(self,element):
        self.find_element(element).clear()
    def get_element_text(self,element):
        return self.find_element(element).text
    # 返回操作
    def press_back(self):
        self.driver.press_keycode(4)
    # 回车操作
    def press_enter(self):
        self.driver.press_keycode(66)
    # 是否存在toast
    def is_toast_exist(self,message):
        message_xpath = By.XPATH,"//*[contains(@text,%s)]" % message
        try:
            self.find_element(message_xpath, 5, 0.1)
            return True
        except TimeoutException:
            return False
    # 获取toast消息
    def get_toast_text(self,message):
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text,%s)]" % message
            return self.find_element(message_xpath,5,0.1)
        else:
            raise Exception("toast没有出现在屏幕上")

    def scroll_page_one_time(self,direction="up"):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        center_x = width / 2
        center_y = height / 2
        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3
        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y
        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确，up/down/left/right")

    def find_element_with_scroll(self, feature, direction="up"):
        page_source = ""
        while True:
            try:
                # 调用BaseAction类里面的find_element方法return 代表退出函数，自然就会退出while循环
                return self.find_element(feature)

            except Exception:

                self.scroll_page_one_time(direction)
                if self.driver.page_source == page_source:
                    print("到底了")
                    raise Exception("没有你定位的元素")
                page_source = self.driver.page_source

    def is_keyword_in_page_source(self,keyword,timeout=10,poll=0.1):
        end_time = time.time() + timeout
        while True:
            if end_time < time.time():
                return False
            if keyword in self.driver.page_source:
                return True
            time.sleep(poll)



