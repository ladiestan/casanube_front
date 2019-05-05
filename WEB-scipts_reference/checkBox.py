# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.implicitly_wait(8)

driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@name='memberPass']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@name='memberPass']").click()
