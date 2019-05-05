# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://www.baidu.com/")
time.sleep(1)
print(driver.capabilities['version'])  # 打印浏览器version的值
driver.quit()
