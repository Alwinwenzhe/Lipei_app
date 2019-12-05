# Author: SH
# Data: 2019/6/6
# Status 
# Comment:该类主要是将excel中的keyword封装
from base.base_driver import BaseDriver
from util.get_by_locator import GetByLocator
import time

class AlwinKeyWord(object):

    def __init__(self,driver):
        self.gb = GetByLocator(driver)

    def alwin_click(self,*args):
        '''
        重新封装appium中的click为excel中的关键字对应
        示例args[0],args[1]对应：partition,key
        :return:
        '''
        self.gb.get_locator(args[0],args[1]).click()

    def alwin_click_all(self,*args):
        '''
        重新封装sappium中的clicks为excel中的关键字对应
        默认点击所有识别对象
        示例args[0],args[1]对应：partition,key
        :return:
        '''
        elements = self.gb.get_locators(args[0],args[1])
        for i in elements:
            i.click()

    def alwin_input(self,*args):
        '''
        重新封装appium中的click为excel中的关键字对应
        示例args[0],args[1],args[2]对应：partition,key,input_content
        :return:
        '''
        self.gb.get_locator(args[0],args[1]).send_keys(args[2])

    def alwin_sleep(self,time_sleep):
        '''
        重新封装休眠时间
        :return:
        '''
        time.sleep(time_sleep)

    def get_element(self,*args):
        '''
        封装期望关键字
        示例args[0],args[1]对应：partition,key
        :return:
        '''
        return self.gb.get_locator(args[0],args[1])


