# coding=utf-8
"""
@Time : 2020/1/6 9:21 
@Author : hzsyy
@FileName : login.py 
@IDE : PyCharm
"""
from selenium import webdriver
from common.readConfig import confParam
from common.GetElement import getElement
ele = getElement("loginPageElement.ini")


def login(driver, url=confParam("url"), account=confParam("account"), password=confParam("password")):
    # 打开登录页
    driver.get(url)

    # 获取账户输入框
    account_input = ele.getElement(driver, 'login', 'account')

    # 获取密码输入框
    passwd_input = ele.getElement(driver, 'login', 'password')

    # 获取登录按钮
    login_button = ele.getElement(driver, 'login', 'loginButton')

    # 输入用户名
    account_input.send_keys(account)

    # 输入密码
    passwd_input.send_keys(password)

    # 点击登录
    login_button.click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    login(driver)

