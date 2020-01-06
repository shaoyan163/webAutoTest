# coding=utf-8
"""
@Time    : 2020/01/04  下午 6:29
@Author  : hzsyy
@FileName: test_home.py
@IDE     : PyCharm
"""
import unittest

import time
from selenium import webdriver

from common.readConfig import confParam
from pages.homePage import homePage
from ddt import ddt, data
from getRootPath import root_dir
import os
from common.readYaml import operYaml
from common.writeLog import writeLog
from common.screen import getScreen



@ddt
class test_价格管理(unittest.TestCase):
    yaml_path = os.path.join(root_dir, "yamlCase", "价格管理.yaml")
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = confParam("url")
        cls.home_Page = homePage(cls.driver, cls.url)
        cls.home_Page.open_home_page()

    def setUp(self):
        pass

    # case_list传进去做数据驱动
    @data(*case_list)
    def test_价格管理(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            account = caseInfo["account"]
            password = caseInfo["password"]
            check = caseInfo["assert"]
            self.__dict__['_testMethodDoc'] = caseName

        # 点击价格设置
        self.home_Page.click_price_manger_btn()

        # 断言
        time.sleep(1)
        getScreen(self.driver, caseName,"price")
        # self.assertIn(check, self.driver.page_source)
        # 写日志文件
        case_info = {"用例名字: ": caseName, "登录账号:": account, "密码: ": password, "断言：": check}
        writeLog(case_info)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()