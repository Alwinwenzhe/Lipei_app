# Author: SH
# Data: 2019/5/17
# Status 
# Comment:

from util.get_by_locator import GetByLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver

class SinaHome(object):
    '''
    新浪首页元素封装
    '''
    def __init__(self,driver):
        self.driver = driver
        self.gl = GetByLocator(self.driver)

    def increate(self):
        '''
        新增元素封装
        :return:
        '''
        return self.gl.get_locator('sina_home', 'increase')

    def chapter(self):
        '''
        文章元素封装
        :return:
        '''
        return self.gl.get_locator('sina_home', 'chapter')

    def chapter(self):
        '''
        文章元素封装
        :return:
        '''
        return self.gl.get_locator('sina_home', 'chapter')

    def get_tost_element(self,message):
        '''
        获取tostelement,
        :param message:
        :return:
        '''
        time.sleep(1)
        tost = ("xpath","//*[contains(@text,"+message+")]")
        return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located)

    def driver_close(self):
        '''
        运行结束关闭driver
        :return:
        '''
        self.driver.quit()
