# Author:
# Data:
# Status
# Comment：yaml文件主要用于读取配置文件，暂时不用该文件
import yaml, time

class OperateYaml(object):

    def __init__(self):
        self.filename = r'D:\Job\python\Script\Lipei_app\config\devices.yaml'

    def read_yaml(self):
        """
        读取yaml
        :return:
        """
        with open(self.filename, 'r', encoding='utf-8') as f:  # encoding解决yaml中 中文问题
            data = yaml.load(f,Loader=yaml.FullLoader)
        return data

    def get_value(self,key,position):
        '''
        通过读取后的yaml文件，取到对应值
        :return:
        '''
        self.data = self.read_yaml()
        return self.data[key][position]

    def read_main(self, str):
        """
        对传入字符串做切割处理
        :return:
        """
        if '/' in str:
            value_len = str.split('/')  # 这里都只会是三级定位，否则出错
            try:
                yaml_value = self.read_yaml()[value_len[0]][value_len[1]][value_len[2]]
            except KeyError as e:
                print("yaml值错误，请检查")
        return yaml_value

    def write_yaml(self, i,device,bp,p):
        '''
        重新把设备信息写入yaml文件
        :param i:
        :param device: 设备名
        :param bp:
        :param port:
        :return:
        '''
        data = self.join_data(i,device,bp,p)
        with open(self.filename, 'w', encoding='utf-8') as yaml_file:
            yaml.dump(data, yaml_file)  # 将新的data数据追加到yaml文件中

    def join_data(self,i,device,bp,p):
        '''
        拼接即将写入yaml的文件
        :return:
        '''
        data = {
            "user_info_" + str(i):{
                "deviceName":device,
                "bp":bp,
                "p":p
            }
        }
        return data

    def clear_data(self):
        '''
        写入之前清理yaml中的数据
        暂时不用清理，会导致运行时获取不到数据，应该是执行顺序引起的，暂未解决
        :return:
        '''
        with open(self.filename,'w') as fr:
            fr.truncate()

if __name__ == '__main__':
    yl = OperateYaml()
    # print(yl.write_yaml())
    print(yl.get_value('user_info_0','deviceName'))