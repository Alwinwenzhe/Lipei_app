# Author: SH
# Data: 2019/5/17
# Status 
# Comment:

from page.sina_home import SinaHome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SinaHomeHandle(object):
    '''
    home页面的业务处理层
    '''
    def __init__(self,driver):
        self.sh = SinaHome(driver)

    def click_increate(self):
        '''
        点击‘+’
        :return:
        '''
        self.sh.increate().click()
        time.sleep(2)

    def click_chapter(self):
        '''
        点击弹出层的‘文章’
        :return:
        '''
        self.sh.chapter().click()
        time.sleep(2)

    def tost_ture_false(self,message):
        '''
        判断tost是否得到
        :return:
        '''
        result = self.sh.get_tost_element(message)
        if result:
            return True
        else:
            return False

    def driver_close(self):
        '''
        运行结束关闭driver
        :return:
        '''
        self.sh.driver_close()