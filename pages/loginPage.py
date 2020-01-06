# encoding: utf-8

"""
@author: shaoyanyan
@file: searchPage.py.py
@time: 2019/12/7 22:37
@ide: pycharm

"""
from selenium import webdriver
from common.readConfig import confParam
from pages.basePage import Page
from common.GetElement import getElement


class LoginPage(Page):
    ele = getElement("loginPageElement.ini")

    def __init__(self, driver, base_url):
        Page.__init__(self, driver, base_url)

    def open_home_page(self):
        # 打开登录页
        self.driver.get(self.base_url)

        # 获取账户输入框
        self.account_input = self.ele.getElement(self.driver, 'login', 'account')

        # 获取密码输入框
        self.passwd_input = self.ele.getElement(self.driver, 'login', 'password')

        # 获取登录按钮
        self.login_button = self.ele.getElement(self.driver, 'login', 'loginButton')

    def input_userName(self, userName):
        # 输入用户名
        self.input_text(self.account_input, userName)

    def input_passwd(self, password):
        # 输入密码
        self.input_text(self.passwd_input, password)

    def click_login_btn(self):
        # 点击登录
        self.click(self.login_button)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = confParam("url")
    login_Page = LoginPage(driver, url)
    login_Page.open_home_page()
    login_Page.input_userName("18042477732")

