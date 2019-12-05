# Author: SH
# Data: 2019/5/19
# Status 
# Comment:
import os

class DosCmd(object):


    def cmd_result(self,command):
        '''
        执行cmd命令，并返回一个list结果
        :param command:
        :return:
        '''
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    def cmd_no_result(self,command):
        '''
        执行cmd命令，不返回结果
        :param command:
        :return:
        '''
        os.system(command)

    def device_swich_input(self):
        '''
        运行前切换为固定输入法，没有返回值
        :return:
        '''
        os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")


    def device_check_input(self):
        '''
        查看当前已连接device中的输入法，并返回
        :return:
        '''
        p = os.popen("adb shell ime list -s")  # 获取的是内存对象
        return p.read()

    def device_print_input(self):
        '''
        打印当前设备已选择输入法
        :return:
        '''
        p = os.popen("adb shell settings get secure default_input_method")  # 获取的是内存对象
        return p.read()

if __name__ == '__main__':
    doc = DosCmd()
    print(doc.cmd_result('adb devices'))