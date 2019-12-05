# Author: SH
# Data: 2019/5/9
# Status 
# Comment:

import xlrd
from xlutils.copy import copy

class OperExcel(object):

    def __init__(self,excel_path=None,i=None):
        '''
        excel_path--excel文件路径
        i--excel的sheet id值
        :param excel_path:
        :param i:
        '''
        if excel_path == None:
            self.excel_path =  r"D:\Job\python\Script\Lipei_app\data\Tiezi.xlsx"
        else:
            self.excel_path = excel_path
        if  i == None:
            self.i= 0
        else:
            self.i = i


    def excel_get_sheet(self):
        """
        获取sheet
        :return: 一个内存地址
        """
        workbook = xlrd.open_workbook(self.excel_path)
        # return workbook.sheets()[self.sheet_id]  # 仅加载指定sheet id
        return workbook.sheets()

    def excel_get_sheets(self):
        '''
        获取sheets之和
        :return:list
        '''
        workbooks = xlrd.open_workbook(self.excel_path)
        sheets = workbooks.sheets()
        return sheets

    def excel_get_lines(self):
        '''
        获取固定sheet_id的行数
        注意需要排除掉第一行
        :return: str
        '''
        tables = self.excel_get_sheet()[self.i]
        return int(tables.nrows)

    def excel_get_id(self, row):
        '''
        获取id值,默认列为0
        :return:
        '''
        return self.excel_get_sheet()[self.i].cell_value(int(row), 0)

    def excel_get_cell(self, row, col):
        '''
        通过行、列获取单元格值
        :param row:
        :param col:
        :return:
        '''
        return self.excel_get_sheet()[self.i].cell_value(int(row), int(col))

    def excel_write_data(self, row, col, value):
        '''
        通过copy，写入excel新数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        book1 = xlrd.open_workbook(self.excel_path)
        book2 = copy(book1)
        sheet = book2.get_sheet(self.i)  # 获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
        sheet.write(row, col, value)       # 这里的value只是一个相应状态，具体接口内容在其下的text中
        book2.save(self.excel_path)