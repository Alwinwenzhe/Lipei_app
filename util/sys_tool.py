# Author: SH
# Data: 2019/5/29
# Status 
# Comment:
import time

class SysTool(object):

    def get_time_tamp(self):
        '''
        获取时间戳
        :return:
        '''
        return int(time.time())


if __name__ == "__main__":
    st = SysTool()
    print(st.get_time_tamp())