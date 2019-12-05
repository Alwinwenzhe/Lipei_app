# Author: SH
# Data: 2019/5/9
# Status 
# Comment:

from util.driver import Driver
from appium import webdriver
from util.cmd import Cmd

class Article_news(object):

    def __init__(self):
        self.cmd = Cmd()
        self.cmd.appium_start()
        driver = Driver()
        self.d = driver.get_driver()

    def send_new(self):
        self.d.find_element_by_name('我的')

if __name__ == '__main__':
    an = Article_news()
    an.send_new()