# coding=utf-8

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage


class Login(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        # self.driver.quit()
        browse = BrowserEngine(self)
        browse.quit_browser()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.type_login_name('superadmin')
        login_page.type_password('123456')
        login_page.click_login_btn()
        try:
            assert '待办事项' in login_page.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()
