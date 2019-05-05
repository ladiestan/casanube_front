# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://news.baidu.com/")
time.sleep(1)
try:
    driver.find_element_by_xpath("//*[@id='news']").is_selected()
    # 元素方法is_selected()返回是是布尔值，用来判断单选或者多选控件是否被选中
    # 或者下拉选择菜单是否选择一个默认的option，都可以通过这个方法去判断。
    print ('Test Pass.')
except Exception as e:
    print ('Test fail', format(e))
