# Author: SH
# Data: 2019/6/11
# Status PASS
# Comment:改用里已调试通过
from keywords.get_data import GetData
from util.get_by_locator import GetByLocator
from util.devices import Devices
from keywords.alwin_key_word import AlwinKeyWord
from base.base_driver import BaseDriver
from base.server import Server
import time, multiprocessing
from util.oper_excel import OperExcel


class KWRunMain(object):

    def __init__(self):
        dr = BaseDriver()
        self.driver = dr.android_driver(0)      #这里参数本来是i，因为不知道怎么传，暂时0代替
        self.gd = GetData()
        self.gb = GetByLocator(self.driver)
        self.ex = OperExcel(excel_path=r'D:\Job\python\Script\Lipei_app\data\KW_Mode.xlsx')

    def run_main(self,i):
        '''
        执行单个用例
        :return:
        '''
        ak = AlwinKeyWord(self.driver)
        key_words = self.gd.key_word(i)
        key_element = self.gd.key_element(i)
        key_element_value = self.gd.key_element_value(i)
        expect_key_word = self.gd.Expected_Key_Word(i)
        expect_key_element = self.gd.Expected_Key_Element(i)
        expect_key_value = self.gd.Expected_Key_value(i)
        if key_element != None:   #关键字操作对象不为空
            key_ele0, key_ele1 = list(key_element.split(","))  # tuple转list
            run_key_word = getattr(ak,key_words)        #反射
            if key_element_value != None:                # 关键字操作对象的值不为空
                run_key_word(key_ele0,key_ele1,key_element_value)
            else:
                run_key_word(key_ele0,key_ele1)
        elif key_element_value != None:                   #仅有关键字和值，如alwin_sleep
            run_key_word = getattr(ak,key_words)
            run_key_word(key_element_value)
        if expect_key_word != None:
            expect_ele0,expect_ele1 = list(expect_key_element.split(","))
            expect_kw = getattr(ak,expect_key_word)
            if expect_key_value != None:                  # 既然expect_key_word不为空，那么expect_key_element肯定不会为空，只有expect_key_value可能为空
                result = expect_kw(expect_ele0,expect_ele1,expect_key_value)
            else:
                result = expect_kw(expect_ele0,expect_ele1)
            self.write_status(i,result)

    def write_status(self,row,result):
        '''
        写入用例执行状态
        row:行
        col:列
        :return:
        '''
        # if result:  #假如result有值，这里需要写入pass
        #     self.ex.excel_write_data(row,10,'pass')    #这里需要写入pass
        # else:
        #     self.ex.excel_write_data(row, 10, 'fail')    #这里需要写入fail
        self.ex.excel_write_data(row, 10, 'pass') if result else self.ex.excel_write_data(row, 10, 'fail')      #三目运算符

    def for_run(self):
        '''
        循环执行用例
        :return:
        '''
        row_count = self.gd.get_lines()
        for i in range(1,row_count):
            self.run_main(i)
        time.sleep(2)
        self.end_run()

    def end_run(self):
        '''
        关闭驱动，结束测试
        :return:
        '''
        self.driver.quit()

def get_devices():
    '''
    返回设备个数，用于多进程
    :return:
    '''
    dev = Devices()
    return len(dev.get_devices())

def appium_init():
    server = Server()
    server.appium_start()

if __name__ == "__main__":
    appium_init()
    time.sleep(20)
    kw = KWRunMain()
    kw.for_run()