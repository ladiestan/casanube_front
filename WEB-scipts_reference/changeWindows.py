# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 全屏
driver.get('https://www.baidu.com')
time.sleep(1)
print (driver.get_window_size())

driver.set_window_size(1280, 800)  # 分辨率 1280*800
time.sleep(1)
print (driver.get_window_size())

driver.set_window_size(1024, 768)  # 分辨率 1024*768
time.sleep(1)
print (driver.get_window_size())
