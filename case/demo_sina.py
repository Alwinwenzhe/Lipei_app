# Author: SH
# Data: 2019/5/14
# Status 
# Comment:

from appium import webdriver
from time import sleep
from util.oper_excel import OperExcel
from util.get_by_locator import GetByLocator
import os

class Driver(object):

    def __init__(self):
        self.oe = OperExcel(self.excel_path())

    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            "unicodeKeyboard": 'true',
            "deviceName": "3XU9X17324W10646",
            "noReset": 'true',
            "platformVersion": "6.0",
            "appPackage": "com.sina.weibo",
            "appActivity": "com.sina.weibo.SplashActivity"  # appium1.7版本之后就应该不需要改配置了

        }
        # 对应的cmd中需先执行：appium -p 4723 -bp 4724 -U 3XU9X17324W10646
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        sleep(8)
        # 登录后进入发布界面
        return driver

    def send_new(self,driver,title,content):
        tel = '\n李老师电话：19981203720'
        content = content + tel
        self.gl = GetByLocator(driver)            #注意这里不要放入init，会导致重复执行
        self.gl.get_locator('sina_home','increase').click()
        self.gl.get_locator('sina_home', 'chapter').click()
        sleep(8)
        self.gl.get_locator('sina_editchapter', 'title').clear()
        self.gl.get_locator('sina_editchapter', 'title').send_keys(title)
        self.gl.get_locator('sina_editchapter', 'content').clear()
        self.gl.get_locator('sina_editchapter', 'content').send_keys(content)
        sleep(8)
        self.gl.get_locator('sina_editchapter', 'next').click()         #这里有问题
        sleep(2)
        self.gl.get_locator('sina_editchapter', 'save').click()
        sleep(2)
        self.gl.get_locator('sina_editchapter', 'titleSave').click()
        sleep(8)

    def excel_path(self):
        '''
        通过相对路径获取目标excel
        通过join来拼接绝对地址
        :return:
        '''
        excel_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'../data/Tiezi.xlsx'))
        return excel_dir

    def circl_send(self):
        '''
        根据excel中数据行数，循环发帖
        :return:
        '''
        driver = self.get_driver()
        line = self.oe.excel_get_lines()
        j = 0
        for i in range(1,line):
            if j < 10:              # 限制数目
                title = self.oe.excel_get_cell(i,0)
                conte = self.oe.excel_get_cell(i,1)
                run = self.oe.excel_get_cell(i,3)
                if run == 'Y':
                    self.send_new(driver,title,conte)
                    j = +1

    def set_input(self):
        '''
        设置输入法为第一个默认输入法
        :return:
        '''
        driver = self.get_driver()
        input_list = driver.available_ime_engines       #注意这里是不用(),源代码：return self.execute(Command.GET_AVAILABLE_IME_ENGINES, {})['value']
        driver.activate_ime_engine(input_list[0])     #设置为第一个输入法

if __name__ == '__main__':
    sina = Driver()
    print(sina.excel_path())
    # sina.circl_send()
    sina.set_input()