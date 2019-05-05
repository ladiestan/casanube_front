# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)
# ActionChains下相关方法在当前的firefox不工作
element = driver.find_element_by_xpath("//*[@id='lg']/img")
actionChains = ActionChains(driver)
actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
# actionChains.context_click(element).send_keys('i').perform()



