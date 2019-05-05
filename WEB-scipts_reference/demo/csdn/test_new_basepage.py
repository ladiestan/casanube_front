# coding=utf-8
import time
from selenium import webdriver

from test1.base_page import BasePage


class TestScreenshot(object):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    basepage = BasePage(driver)

    def test_take_screen(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(1)
        self.basepage.take_screenshot()
        self.basepage.quit_browser()


test = TestScreenshot()
test.test_take_screen()
