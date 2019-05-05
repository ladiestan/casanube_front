# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        #  self.driver.find_element_by_id('kw').send_keys('selenium')
        #  time.sleep(1)
        #  try:
        #      assert 'selenium' in self.driver.title
        #      print ('Test Pass.')
        #  except Exception as e:
        #      print ('Test Fail.', format(e))
        homepage = HomePage(self.driver)
        # 到一个页面，第一件事情是初始化这个页面的一个页面对象实例。
        # 注意，一定要带self.driver，不然会报错，这个self.driver，可以这样理解：在当前测试类里面，
        # self.driver是来自浏览器引擎类中方法得到的，在初始化一个页面对象的时候，
        # 也把这个来自浏览器引擎类的driver给赋值给当前的页面对象，这样，才能执行页面对象或者基类里面的相关driver方法。
        # 写多了selenium的自动化脚本，你会明白，最重要的是保持前后driver的唯一性。

        homepage.type_search('selenium')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()
