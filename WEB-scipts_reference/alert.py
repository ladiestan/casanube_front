# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
time.sleep(1)

driver.execute_script("window.alert('这是一个alert弹框。');")  # 注意这里的分号是英文输入法的分号，不能用中文
