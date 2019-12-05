# Author: SH
# Data: 2019/6/6
# Status 
# Comment:该py文件主要是对excel中各项数据获取进行封装

from util.oper_excel import OperExcel

class GetData(object):

    def __init__(self):
        self.oe = OperExcel(excel_path=r'D:\Job\python\Script\Lipei_app\data\KW_Mode.xlsx')

    def key_word(self,row):
        '''
        row--行这个数据需要单独传入
        关键字数据获取封装
        :return:
        '''
        return self.oe.excel_get_cell(row,4)

    def key_element(self,row):
        '''
        row--行这个数据需要单独传入
        关键字操作对象元素数据获取封装
        :param row:
        :return:
        '''
        temp = self.oe.excel_get_cell(row, 5)
        if temp == '':                           # 处理可能出现的空值
            return None
        else:
            return temp

    def key_element_value(self,row):
        '''
        row--行这个数据需要单独传入
        关键字操作对象元素的值数据获取封装
        :param row:
        :return:
        '''
        temp = self.oe.excel_get_cell(row, 6)
        if temp == '':
            return None
        else:
            return temp

    def Expected_Key_Word(self,row):
        '''
        row--行这个数据需要单独传入
        期望关键字获取封装
        :param row:
        :return:
        '''
        temp = self.oe.excel_get_cell(row, 7)
        if temp == '':
            return None
        else:
            return temp

    def Expected_Key_Element(self,row):
        '''
        row--行这个数据需要单独传入
        期望关键字操作对象元素数据获取封装
        :param row:
        :return:
        '''
        temp = self.oe.excel_get_cell(row, 8)
        if temp == '':
            return None
        else:
            return temp

    def Expected_Key_value(self,row):
        '''
        row--行这个数据需要单独传入
        期望关键字获取封装
        :param row:
        :return:
        '''
        temp = self.oe.excel_get_cell(row, 9)
        if temp == '':
            return None
        else:
            return temp

    def exec_status(self,row):
        '''
        用例执行状态
        :return:
        '''
        temp = self.oe.excel_get_cell(row, 10)
        if temp == '':
            return None
        else:
            return temp

    def get_lines(self):
        '''
        获取当前sheet的行数
        :return:
        '''
        return self.oe.excel_get_lines()


if __name__ == "__main__":
    gd = GetData()
    print(gd.key_element(1))
    print(gd.get_lines())
