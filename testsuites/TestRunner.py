# coding=utf-8
import sys
sys.path.append('..')
import unittest
import testsuites
from testsuites.test_search import BaiduSearch
from testsuites.test_get_page_title import GetPageTitle
import HTMLTestRunner
import os
import unittest
import time

# 第一种方式
# suite = unittest.TestSuite()
# suite.addTest(BaiduSearch('test_baidu_search'))
# suite.addTest(BaiduSearch('test_search2'))
# suite.addTest(GetPageTitle('test_get_title'))
# 第二种方式
# suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
# 第三种方式
# suite = unittest.TestLoader().discover("testsuites")
# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = file(HtmlFile, "wb")
# 构建suite
suite = unittest.TestLoader().discover("testsuites")

if __name__ == '__main__':
    # 执行用例
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
