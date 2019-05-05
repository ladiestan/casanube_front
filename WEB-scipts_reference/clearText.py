# coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium")
try:
    driver.find_element_by_id("kw").clear()  # 调用clear()方法去清除
    print ('test pass: clean successful')
except Exception as e:
    print ("Exception found", format(e))
