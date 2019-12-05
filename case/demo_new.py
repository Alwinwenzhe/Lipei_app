# Author: SH
# Data: 2019/5/14
# Status  FAIL
# Comment: 内容中输入数字后的中文变英文
from appium import webdriver
from time import sleep
from util.oper_excel import OperExcel
import sys
import os
from util.cmd import Cmd

class Driver(object):

    def __init__(self):
        self.oe = OperExcel()
        self.cmd =Cmd()

    def start_appium(self):
        self.cmd.appium_start()

    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            "resetKeyboard":"true",
            "unicodeKeyboard": 'true',
            "deviceName": "3XU9X17324W10646",
            "noReset": 'true',
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.SplashBadgeActivity"  # appium1.7版本之后就应该不需要改配置了

        }
        # 对应的cmd中需先执行：appium -p 4723 -bp 4724 -U 3XU9X17324W10646
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        sleep(8)
        driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='4']").click()
        sleep(3)
        driver.find_element_by_xpath("//android.widget.LinearLayout[@index='6']").click()
        sleep(3)
        return driver

    def new_send(self,driver,title,conten):
        driver.find_element_by_xpath("//android.widget.ImageView[@index='0']/../following-sibling::android.view.ViewGroup/android.widget.ImageView").click()
        sleep(10)
        driver.find_element_by_xpath("//android.widget.EditText[@index='0']").clear()
        driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys(title)
        sleep(5)
        tel = '\n李老师电话:19981203720'
        conten = conten + tel
        driver.find_element_by_xpath(
            "//android.widget.EditText[@index='0']/../following-sibling::android.view.View/android.view.View/android.view.View").clear()
        driver.find_element_by_xpath("//android.widget.EditText[@index='0']/../following-sibling::android.view.View/android.view.View/android.view.View").send_keys(conten)
        sleep(10)
        # driver.find_element_by_xpath("//android.widget.TextView[@index='0']/../../following-sibling::android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageButton[@index='1']").send_keys(r"D:\Job\python\Script\Robot\Lipei_auto\data\pic\baoming.jpg")
        # 上面这个元素定位已验证没问题 但是appium中只能通过相册选择图片附件

        # driver.find_element_by_xpath(
        #     "//android.widget.TextView[@index='0']/../../following-sibling::android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageButton[@index='1']").click()
        # driver.wait_activity("com.test.camera", 2)
        # # 下方发图暂时未成功
        # driver.find_element_by_xpath("//com.ss.android.article.news:id/ccr[@index='1']").click()
        # driver.find_element_by_xpath("//com.ss.android.article.news:id/ba3[@index='1']").click()
        # # pic_list = driver.find_elements_by_xpath("//com.ss.android.article.news:id/ba3")
        # sleep(10)
        driver.find_element_by_xpath("//android.widget.TextView[@index='2']").click()
        sleep(3)


    def circl_send(self):
        '''
        根据excel中数据行数，循环发帖
        :return:
        '''
        driver = self.get_driver()
        line = self.oe.excel_get_lines()
        for i in range(1,line):
            title = self.oe.excel_get_cell(i,0)
            conte = self.oe.excel_get_cell(i,1)
            run = self.oe.excel_get_cell(i,3)
            if run == 'Y':
                self.new_send(driver,title,conte)

    def excel_path(self):
        '''
        通过相对路径获取目标excel
        通过join来拼接绝对地址
        :return:
        '''
        excel_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'../data/Tiezi.xlsx'))
        return excel_dir

if __name__ == '__main__':
    d = Driver()
    # d.start_appium()
    # sleep(20)
    d.circl_send()
