# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(1)
# 方法一利用python中Assert方法，采用包含判断，u代表unicode，python 2需要
try:
    assert u"百度一下" in driver.title
    print ('Assertion test pass.')
except Exception as e:
    print ('Assertion test fail.', format(e))
# 方法二通过if方法，采用完全相等方法
if u"百度一下，你就知道" == driver.title:
    print ('Assertion test pass.')
else:
    print ('Assertion test fail.')

print driver.title
