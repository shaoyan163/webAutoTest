# coding=utf-8
"""
@Time    : 2019/05/24  下午 12:42
@Author  : hzsyy
@FileName: run.py
@IDE     : PyCharm
"""
import time
import unittest
from BeautifulReport import BeautifulReport

from getRootPath import root_dir
import os

test_dir = os.path.join(root_dir, "testcase")
reportPath = os.path.join(root_dir, "report")
print(test_dir)
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

now = time.strftime("%Y-%m-%d %H_%M_%S")
reportName = now + '测试报告.html'
description = "左中右UI自动化测试报告"
BeautifulReport(discover).report(filename=reportName, description=description, report_dir=reportPath)
report = os.path.join(reportPath, reportName)

# 发送邮件
# sendEmail.email(report)

if __name__ == "__main__":
    screenshot_path = os.path.join(root_dir, "pictures") + "q" + ".png"
    print(screenshot_path)