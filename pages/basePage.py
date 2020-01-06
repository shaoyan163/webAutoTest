# coding=utf-8

# pages基类
class Page(object):
    """
        Page基类，所有page都应该继承该类
    """

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def input_text(self, loc, text):
        loc.send_keys(text)

    def click(self, loc):
        loc.click()

    def get_title(self):
        return self.driver.title