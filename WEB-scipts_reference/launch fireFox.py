# -*-coding:utf-8-*-
from selenium import webdriver   # 导入webdriver包
 
driver = webdriver.Firefox()    # 初始化一个火狐浏览器实例：driver
 
driver.maximize_window()        # 最大化浏览器
 
driver.get("https://www.baidu.com")  # 通过get()方法，打开一个url站点
 
driver.quit()     # 关闭并退出浏览器
