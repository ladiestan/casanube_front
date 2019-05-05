# coding=utf-8
import time
from selenium import webdriver


class GetSubString(object):

    def get_search_result(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(8)

        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        search_result_string = driver.find_element_by_xpath("//*/div[@class='nums']").text
        print (search_result_string)

        new_string = search_result_string.split(u'约')[1]  # 第一次切割得到 xxxx个，[1]代表切割右边部分
        print (new_string)
        last_result = new_string.split(u'个')[0]  # 第二次切割，得到我们想要的数字 [0]代表切割参照参数的左边部分
        print (last_result)


getstring = GetSubString()
getstring.get_search_result()
