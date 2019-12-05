# Author: SH
# Data: 2019/5/9
# Status 
# Comment:

from appium import webdriver
from time import sleep
from util.cmd import Cmd

class Driver(object):

    def __init__(self):
        self.cmd = Cmd()

    def start_appium(self):
        '''
        调试改driver临时增加的函数
        :return:
        '''
        self.cmd.appium_start()

    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            "unicodeKeyboard": 'true',                      #input chinese
            "deviceName": "3XU9X17324W10646",
            "noReset": True,
            "platformVersion": "6.0",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.SplashBadgeActivity",  # appium1.7版本之后就应该不需要改配置了
            "resetKeyboard": True
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        sleep(8)
        return driver
        #对应的cmd中需先执行：appium -p 4723 -bp 4724 -U 3XU9X17324W10646

    def send(self):
        self.start_appium()
        d = self.get_driver()
        d.find_element_by_name("我的")
        sleep(20)

if __name__ == '__main__':
    d = Driver()
    d.send()