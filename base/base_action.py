# 封装定位一个元素的方法
# 封装定位多个元素的方法
# 定位元素，返回元素，需要传入特征feature,
# 设置显式等待，设置默认等待时间，频率。实际工作中，可以根据实际需要，修改等待时间
# 封装点击，输入，清空的操作
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



