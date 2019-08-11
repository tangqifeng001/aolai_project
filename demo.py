from appium import webdriver
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.102:5555'

desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# desired_caps["unicodeKeyboard"] = True
# desired_caps["resetKeyboard"] = True
desired_caps['automationName'] = 'Uiautomator2'
# # 不会重置应用
# desired_caps['noReset'] = no_reset

driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)
while True:
    try:
        driver.find_element_by_xpath("//*[@text='关于手机']").click()
        break
    except Exception:
        driver.swipe(100,2000,100,1000)
