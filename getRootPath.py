# coding=utf-8
"""
@Time    : 2019/05/25  上午 11:14
@Author  : hzsyy
@FileName: getRootPath.py
@IDE     : PyCharm
"""
import os

root_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    print(root_dir)
    picture_path = os.path.join(root_dir,"pictures")
    print(os.path.join(picture_path,"123" + ".png"))
    print(os.path.join(os.path.join(root_dir, "elements"), "WebElement.ini"))