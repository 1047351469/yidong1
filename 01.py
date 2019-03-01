import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

# server 启动参数
desired_caps = {}
# 安卓设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# appium服务端
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.page_source
driver.current_package
driver.current_activity
driver.start_activity("","")
driver.close_app()
driver.install_app("")
driver.is_app_installed("")
driver.remove_app("")
driver.push_file("","")
driver.pull_file("")
driver.background_app(5)
time.sleep(2)
a = driver.find_element_by_id("")
driver.find_elements_by_id("")
b = driver.find_element_by_class_name("")
driver.find_elements_by_class_name("")
driver.find_element_by_xpath("")
driver.find_elements_by_xpath("")
WebDriverWait(driver,5,1).until(lambda x: x.find_element_by_id(""))
driver.find_element_by_id("").click()
driver.find_element_by_id("").send_keys()
driver.find_element_by_id("").clear()
l = driver.find_elements_by_class_name("")
for i in l:
    print(i.text,i.get_attribute("name"))
driver.find_element_by_id("").location
driver.swipe(1,2,3,4,5)
driver.scroll(a, b)
driver.drag_and_drop(a, b)
TouchAction(driver).tap(a).perform()
TouchAction(driver).press(a).wait(5).release().long_press(a, 5).move_to(0,10).perform()
# 移动
driver.device_time
driver.get_window_size()
driver.keyevent(24)
driver.open_notifications()
driver.set_network_connection(1)
driver.network_connection
driver.quit()
driver.get_screenshot_as_file("")
