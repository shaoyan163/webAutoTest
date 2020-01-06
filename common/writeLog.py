#coding=utf-8
from common.logger import Log

log = Log()


def writeLog(kwargs):
    log.info("#" * 100 + "开始测试" + "#" * 100)
    for key in kwargs.keys():
        log.info("{} {}".format(key, kwargs[key]))
    log.info("#" * 100 + "测试结束" + "#" * 100)


if __name__ == "__main__":
    case_info = {"用例名字: ": "123", "登录账号:": "qwe", "密码: ": "qwe", "断言：": "wer"}
    writeLog(case_info)