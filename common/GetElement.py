# encoding: utf-8

"""
@author: shaoyanyan
@file: GetElement.py.py
@time: 2019/12/7 21:57
@ide: pycharm
"""
import time

from selenium.webdriver.support.ui import WebDriverWait
import configparser
import os
from selenium import webdriver
from getRootPath import root_dir


class getElement():
    def __init__(self, elementFile):
        self.elementPath = os.path.join(root_dir, "elements")
        self.elementIni = os.path.join(self.elementPath, elementFile)

    def getElement(self, driver, section, option):
        try:
            f = configparser.ConfigParser()
            f.read(self.elementIni)  # 读配置文件内容到内存中
            locators = f.get(section, option).split(':')
            # 获取定位方式
            locaMethod = locators[0]
            # 获取定位表达式
            locaExpression = locators[1]
            # 通过显示等待的方式获取页面的元素
            element = WebDriverWait(driver, 5).until(lambda x: x.find_element(locaMethod, locaExpression))
        except Exception as e:
            raise e
        else:
            return element


if __name__ == '__main__':
    ele = getElement("loginPageElement.ini")
    driver = webdriver.Chrome()
    driver.get('https://travel-test.wgjev.net/#/login')
    element = ele.getElement(driver, 'login', 'account')
    element.send_keys('18042477732')
    element = ele.getElement(driver, 'login', 'passwd')
    element.send_keys('syy0107!@#$')
    time.sleep(2)
    driver.quit()
