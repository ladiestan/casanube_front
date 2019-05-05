# coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
try:
    driver.find_element_by_name("wd")  # 这里百度搜索输入框有name = 'wd'这个节点信息
    print ('test pass: element found by name value')
except Exception as e:
    print ("Exception found", format(e))

driver.quit()
