# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')

element = driver.find_element_by_tag_name('body')
element.send_keys(Keys.CONTROL + 'a')
