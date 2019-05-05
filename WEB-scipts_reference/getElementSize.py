# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com/")
time.sleep(1)
search_btn = driver.find_element_by_id('su')
print (search_btn.size)
