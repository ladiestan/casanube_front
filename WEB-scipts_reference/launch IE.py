# -*- coding:utf-8 -*-
from selenium import webdriver

driver = webdriver.Ie()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
driver.quit()