# Author: SH
# Data: 2019/5/17
# Status 
# Comment:

from handle.sina_chapter_handle import SinaChapterHandle
from handle.sina_home_handle import SinaHomeHandle
import time
from base.base_driver import BaseDriver
from util.oper_excel import OperExcel
from handle.sys_sdk import SysSdk
from business.sina_choose_pics_business import SinaChoosePicsBusiness
class SinaSendChapterBusiness(object):
    '''
    处理新浪发布文章流程
    '''

    def __init__(self,i):
        self.driver = BaseDriver().android_driver(i)        # driver都从business生产并传递，底层不重复生产
        self.sch = SinaChapterHandle(self.driver)
        self.shh = SinaHomeHandle(self.driver)
        self.oe = OperExcel()
        self.ss = SysSdk(self.driver)
        self.cp = SinaChoosePicsBusiness(self.driver)

    def send_chapter(self,title,content):
        '''
        发布文章流程
        :return:
        '''
        self.shh.click_increate()
        self.shh.click_chapter()
        self.sch.input_title(title)
        self.sch.input_content(content)
        time.sleep(10)
        self.sch.click_pic()
        time.sleep(1)
        self.sch.choose_pic(self.ss.get_sys_pic_activity())
        self.sch.click_next()
        time.sleep(1)
        self.sch.save_chapter()
        time.sleep(5)
        self.sch.send_chapter()
        time.sleep(8)
        #self.shh.driver_close()

    def circl_send_sina(self):
        '''
        根据excel中数据行数，循环发帖
        :return:
        '''
        line = self.oe.excel_get_lines()
        j = 0
        for i in range(1,line):   #过滤掉第一行
            if j < 10:              # 限制数目
                title = self.oe.excel_get_cell(i,0)
                conte = self.oe.excel_get_cell(i,1)
                content = conte + "\n联系电话(微信)：19981203720"
                run = self.oe.excel_get_cell(i,3)
                if run == 'Y':
                    self.send_chapter(title,content)
                    time.sleep(12)          #增加每条发布时间间隔，太长了，会是去连接的
                    j = +1

    def set_input(self):
        '''
        设置输入法为第一个默认输入法
        :return:
        '''
        input_list = self.driver.available_ime_engines       #注意这里是不用(),源代码：return self.execute(Command.GET_AVAILABLE_IME_ENGINES, {})['value']
        self.driver.activate_ime_engine(input_list[0])     #设置为第一个输入法

