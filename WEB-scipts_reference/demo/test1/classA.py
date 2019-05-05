# coding = utf-8

from selenium import webdriver
import time


class ClassA(object):

    def open_baidu(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.baidu.com")
        time.sleep(1)
        driver.quit()
