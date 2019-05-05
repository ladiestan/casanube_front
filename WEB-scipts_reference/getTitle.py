# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://www.baidu.com/")
time.sleep(1)
driver.find_element_by_link_text("新闻").click()
time.sleep(1)
print (driver.title)  # title方法可以获取当前页面的标题显示的字段
driver.quit()
