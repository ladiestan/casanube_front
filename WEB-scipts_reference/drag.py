# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://tieba.baidu.com/index.html")
time.sleep(1)

target_elem = driver.find_element_by_link_text("地区")
driver.execute_script("return arguments[0].scrollIntoView();", target_elem)  # 用目标元素参考去拖动
# driver.execute_script("scroll(0,2400)") # 这个是第二种方法，比较粗劣，大概的拖动
