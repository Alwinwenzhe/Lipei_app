# Author: SH
# Data: 2019/5/16
# Status 
# Comment:

import configparser

class OperIni():

    def __init__(self):
        self.data = self.read_init()    # 默认执行到内存中

    def read_init(self):
        read_init = configparser.ConfigParser()
        read_init.read(r'D:\Job\python\Script\Lipei_app\config\element.ini', encoding="utf-8")  # 这里读取后，不能赋值给变量，要不然就只能获取路径,注意编码是针对ini包含中文 路徑寫法需要注意
        return read_init

    def read(self,partition,key):
        '''
        读取ini文件并返回特定值
        :param partition:
        :param key:
        :return:
        '''
        try:
            us = self.data.get(partition,key)
        except:     #处理partition或key不存咋是，返回none
            us = None
        return us

if __name__ == '__main__':
    one = OperIni()
    u = one.read('sina_home', 'increase')
    print (u)