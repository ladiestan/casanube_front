# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://www.baidu.com/")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)

driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__submit']").click()
# 断言方法一
# 直接把字段写入XPath表达式，如果通过该XPath能定位到元素，说明这个错误字段已经在页面显示；
try:
    error_message = driver.find_element_by_xpath(
        "//*[@id='TANGRAM__PSP_8__error' and text()='请您填写手机/邮箱/用户名']").is_displayed()
    print ("Test pass. the error message is display.")
except Exception as e:
    print ("Test fail.", format(e))

# 断言方法二，重点
# 要获取到目标元素的text的值，需要定义一个目标元素element，
# 然后通过element.text方法得到字符串，注意不是element.text(),这个方法是没有带小括号的。
# 方法二是通过该目标元素节点，然后通过element.text得到值，在拿得到的text值取和期待的结果去字符串匹配。
# 建议第二个方法。

error_mes = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__error']").text
try:
    assert error_mes == u'请您填写手机/邮箱/用户名'
    print ('Test pass.')
except Exception as e:
    print ("Test fail.", format(e))
