# Author: SH
# Data: 2019/5/9
# Status 
# Comment:

import os
import re
import appium
from time import sleep

class Cmd(object):

    def cmd_command(self, cmd='adb devices'):
        '''
        执行cmd命令并返回结果
        :param command:
        :return:返回结果中可能存在多个设备
        '''
        p = os.popen(cmd)  # 获取的是内存对象
        return p.read()


    def cmd_devices(self):
        '''
        从cmd结果中剥离出设备列表并返回
        :param list_devices:
        :return:
        '''
        temp_1 = self.cmd_command().split('\n')  # 通过换行符第一次划分
        temp_2 = temp_1[1::]  # 去掉第一个无用值
        for i in temp_2:  # 去掉空值
            if len(i) < 1:
                temp_2.remove(i)
        return temp_2


    def re_appium_str(self, rule=r'[0-9a-zA-Z]{16}'):
        '''
        本方法转为appium启动服务：通过正则过滤或替换目标元素,并返回
        :param content:
        :return:
        '''
        result_list = []
        for i in self.cmd_devices():
            if i:  # 去掉传入的空值
                result = re.search(rule, i).group()  # r'[0-9a-zA-Z]{16}':匹配1到9，a到z，A到Z组合起来长度为16的结果
                result_list.append(result)
        return result_list


    def appium_start(self):
        '''
        启动appium服务，这里暂时写的是一个设备启动,version暂时不知道怎么处理
        :param devices_list:
        :return:
        '''
        p = 4723
        devices_list = self.re_appium_str()
        for i in devices_list:
            os.system(              #system仅执行不返回结果
                "appium -a 127.0.0.1 -p {0} --platform-name Android --automation-name Appium --device-name {1} --session-override".format(
                    p, i))
                # "appium -a 127.0.0.1 -p 4723 -bp 4724 -U 3XU9X17324W10646 --no -reset --session -override"
            p += 1
        sleep(20)

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


if __name__ == "__main__":
    cmd = Cmd()
    cmd.appium_start()