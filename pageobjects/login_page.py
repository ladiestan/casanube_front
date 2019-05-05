# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):
    login_name = "xpath=>//input"
    password = "xpath=>//input[@type='password']"
    login_btn = "xpath=>//button"

    def type_login_name(self, text):
        self.type(self.login_name, text)

    def type_password(self, text):
        self.type(self.password, text)

    def click_login_btn(self):
        self.click(self.login_btn)
