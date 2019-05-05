# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
driver.find_element_by_xpath("//*[@id='su']").click()

time.sleep(2)
# 第二个判断方法
ele_string = driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a").text
if (ele_string == u"Selenium - Web Browser Automation"):
    print "测试成功，结果和预期结果匹配！"
driver.quit()
