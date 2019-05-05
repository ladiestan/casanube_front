# coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
try:
    driver.find_element_by_partial_link_text("主页").click()
    print ('test pass: element found by partial link text')
except Exception as e:
    print ("Exception found", format(e))

driver.quit()
# 选择partial link text的时候，需要选择一个比较唯一的字段，来区分这个元素。
