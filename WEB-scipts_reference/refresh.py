# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
time.sleep(2)
try:
    driver.refresh()  # 刷新方法 refresh
    print ('test pass: refresh successful')
except Exception as e:
    print ("Exception found", format(e))
driver.quit()
