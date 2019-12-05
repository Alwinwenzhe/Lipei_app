# Author:
# Data:
# Status
# Comment:excel中请求内容如果是json，那么json内容单独存放在json.json文件中，通过该py文件读取json内容

import json

class OperateJson(object):

    def __init__(self):
        self.file_path = r'dataconfig\json.json'
        #如果构建函数中增加了下行代码会导致用例:第一个用例修改了json，第二个用例读取最新json值会读到旧值；因为初始化就会将json文件读入到内存，的第二次会督导内存中的值
        # self.json_data = self.read_json()

    def read_json(self):
        """
        读取json文件
        :return:
        """
        with open(self.file_path, 'r', encoding='UTF-8') as fp:
            data = json.load(fp)
            return data

    def get_json_value(self, id):
        """
        获取对应json值,这里会读到上一次token信息
        :param id:
        :return:
        """
        return self.read_json()[id]

    def write_json_value(self, key, value):
        """
        将新值写入json原有数据中，如果值相同，则覆盖
        每次写入一组数据
        :param key:
        :param value:
        :return:
        """
        # 单独读取文件
        init_json = self.read_json()
        init_json[key] = value
        with open(self.file_path, 'w', encoding='UTF-8') as f:
            json.dump(init_json, f)


if __name__ == '__main__':
    rj = OperateJson()
    # print(rj.get_json_value('login1'))
    rj.write_json_value('aa', 'DEFDS')
    print(rj.read_json())
