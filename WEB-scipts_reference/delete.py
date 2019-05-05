# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')

element = driver.find_element_by_id('kw')
element.send_keys("Selenium automation")
time.sleep(1)
element.send_keys(Keys.CONTROL + 'a')
element.send_keys(Keys.BACKSPACE)
