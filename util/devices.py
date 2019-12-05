# Author: SH
# Data: 2019/5/19
# Status 
# Comment:
from util.dos_cmd import DosCmd

class Devices(object):

    def __init__(self):
        self.cmd = DosCmd()

    def get_devices(self):
        '''
        获取设备列表
        :return:
        '''
        device_list = []
        list = self.cmd.cmd_result("adb devices")
        try:
            devices = list[1::]         #第一个打印信息排除
            if len(devices) >= 1:
                for i in devices:
                    device = i.split("\t")
                    if device[1] == 'device':   #排除得到的是非设备类信息
                        device_list.append(device[0])
        except ValueError as v:
            print('设备接入异常，请ADB核实')
        finally:
            return device_list

if __name__ == "__main__":
    dev = Devices()
    print(dev.get_devices())