# coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
try:
    driver.find_element_by_link_text("新闻")
    print ('test pass: element found by link text')
except Exception as e:
    print ("Exception found", format(e))

driver.quit()
# 凡是看到链接元素上面有文字描述的都可以采取find_element_by_link_text（）方法来进行元素定位。
# 这里提一下前面XPath定位中的知识，通过text()这个XPath中的函数也可以达到类似link text定位的目的。
# 这个“新闻”链接元素的XPath表达式可以这样写：//*/div[@id='u1']/a[text()='新闻']
