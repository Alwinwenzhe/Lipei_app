# Author: SH
# Data: 2019/5/20
# Status 
# Comment:
from util.port import Port
from util.devices import Devices
from util.dos_cmd import DosCmd
import multiprocessing, time
from util.operate_yaml import OperateYaml
from base.base_driver import BaseDriver

class Server(object):

    def __init__(self):
        self.p = Port()
        self.dev = Devices()
        self.doc = DosCmd()
        self.oy = OperateYaml()
        self.devices_list = self.dev.get_devices()

    def create_appium_command(self,i):
        '''
        根据设备列表拼接出对应appium启动命令
        :return:
        '''
        command_list = []
        appium_port_list = self.p.create_port_list(4000)  # 根据获取设备信息创建对应端口列表
        appium_bp_port_list = self.p.create_port_list(4500)
        if self.devices_list != None:
            # for i in range(len(devices_list)):  # 根据设备信息长度，对3个list进行for循环，依次去除并拼接好敏灵
            command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(
                appium_bp_port_list[i]) + " -U " + str(self.devices_list[i]) + " --no-reset --session-override" + " --log D:\Job\python\Script\Lipei_app\\report\log\\" + str(self.devices_list[i]) + ".log"        #将log写入对应文件
            command_list.append(command)
            self.oy.write_yaml(i, str(self.devices_list[i]), str(appium_bp_port_list[i]), str(appium_port_list[i]))
            return command_list

    def start_server(self, i):
        '''
        启动appium服务，变量i通过多线程appium_start传入
        :param i:
        :return:
        '''
        self.start_list = self.create_appium_command(i)  # 带self的就表示对象本身，属于该py全局的，这里就可以认为定义全局变量
        self.doc.cmd_no_result(self.start_list[0])          #注意这里不能传i，仅能是0
        time.sleep(20)

    def appium_start(self):
        '''
        根据接入设备多线程启动服务
        :return:
        '''
        self.kill_servee()
        # self.oy.clear_data()
        for i in range(len(self.devices_list)):  # 根据得到的启动命令列表长度，确认该启动几个线程
            appium_server = multiprocessing.Process(target=self.start_server, args=(i,))
            appium_server.start()

    def kill_servee(self):
        '''
        查找appium进程：tasklist | find "node.exe"；
        杀死所有node进程：taskkill -F -PID "node.exe"
        :return:
        '''
        command = 'tasklist | find "node.exe"'
        task_msg = self.doc.cmd_result(command)
        if len(task_msg) > 0:
            self.doc.cmd_no_result('taskkill -F -PID node.exe')

    def close_driver(self,i):
        dr = BaseDriver()
        dr.close_driver(i)

if __name__ == "__main__":
    ser = Server()
    ser.appium_start()
    time.sleep(10)
    # ser.kill_servee()