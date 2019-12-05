# Author: SH
# Data: 2019/7/8
# Status
# Comment:
from appium import webdriver

from appium import webdriver
from time import sleep
from util.get_by_locator import GetByLocator
#
# start_cmd = "appium -p 4723 -bp 4724 -U 3XU9X17324W10646 --no-reset --session-override"
# os.system(start_cmd)

class Driver(object):

    def __init__(self):
        self.driver = self.get_driver()

    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            # "resetKeyboard":"true",
            "unicodeKeyboard": 'true',
            "deviceName": "3XU9X17324W10646",
            "noReset": 'true',
            # "platformVersion": "6.0",            # OPPO-a73也可正常运行，所以不需要这个版本号
            "appPackage": "com.haidilao",
            "appActivity": "com.haidilao.hailehui.biz.ActivityWelcome"  # appium1.7版本之后就应该不需要改配置了
        }
        # 对应的cmd中需先执行：appium -p 4723 -bp 4724 -U 3XU9X17324W10646
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        sleep(8)
        # 登录后进入发布界面
        return driver

    def game_1(self):
        '''
        自动玩捞菜游戏
        :param driver:
        :param title:
        :param content:
        :return:
        '''
        self.gl = GetByLocator(self.driver)  # 注意这里不要放入init，会导致重复执行
        self.gl.get_locator('haidi_home', 'game').click()
        sleep(5)
        self.gl.get_locator('haidi_home','game1').click()       #这里虽是进h5，但是只要等待足够时间，就可以点击成功，不需要切换activity

    def circl_send(self):
        '''
        根据excel中数据行数，循环发帖
        :return:
        '''
        driver = self.get_driver()
        line = self.oe.excel_get_lines()
        j = 0
        for i in range(1, line):
            if j < 10:  # 限制数目
                title = self.oe.excel_get_cell(i, 0)
                conte = self.oe.excel_get_cell(i, 1)
                run = self.oe.excel_get_cell(i, 3)
                if run == 'Y':
                    self.send_new(driver, title, conte)
                    j = +1


if __name__ == '__main__':
    haidilao = Driver()
    haidilao.game_1()