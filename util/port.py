# Author: SH
# Data: 2019/5/20
# Status 
# Comment:
from util.dos_cmd import DosCmd
from util.devices import Devices

class Port(object):

    def __init__(self):
        self.dc = DosCmd()
        self.devices = Devices()

    def port_is_used(self, port_num):
        # 查看端口是否被占用：False--没有被占用
        command = 'netstat -ano | findstr ' + str(port_num)  # 字符串只能和字符串拼接
        flag = None
        result_list = self.dc.cmd_result(command)
        if len(result_list) > 0:
            flag = False    #被占用
        else:
            flag = True  # true时，就未被占用
        return flag

    def create_port_list(self, start_port):
        '''
        start_port:创建appium的开始端口
        调用两次就可以生成p或bp端口
        :param start_port:
        :return:
        '''
        port_list = []
        if self.devices.get_devices() != None:
            while len(port_list) != len(self.devices.get_devices()):  # port少于设备就执行
                if self.port_is_used(start_port):  # 检测端口是否被占用
                    port_list.append(start_port)
                start_port += 1  # 端口自增
            return port_list
        else:  # 判定devices_list返回的是none时，提示生成失败
            print("adb没有检测到连接的手机设备")

if __name__ == '__main__':
    po = Port()
    print(po.create_port_list(4723))
    print(po.create_port_list(4823))