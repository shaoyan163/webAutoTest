# encoding: utf-8

"""
@author: shaoyanyan
@file: searchPage.py.py
@time: 2019/12/7 22:37
@ide: pycharm

"""
import time

from selenium import webdriver
from common.readConfig import confParam
from common.login import login
from pages.basePage import Page
from common.GetElement import getElement


class homePage(Page):
    ele = getElement("loginPageElement.ini")

    def __init__(self, driver, base_url):
        Page.__init__(self, driver, base_url)

    def open_home_page(self):
        # 进入home页
        login(self.driver)

        time.sleep(2)
        # 刷新页面
        self.driver.refresh()

        # 定位展开侧边元素
        expand_sidebar = self.ele.getElement(self.driver, 'home', 'expandSidebar')

        # 点击展开侧边
        expand_sidebar.click()

        # 获取价格设置
        self.price_manger_btn = self.ele.getElement(self.driver, 'home', 'priceManger')

    def click_price_manger_btn(self):
        # 点击价格设置
        self.click(self.price_manger_btn)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = confParam("url")
    login_Page = homePage(driver, url)
    login_Page.open_home_page()
    login_Page.click_price_manger_btn()


