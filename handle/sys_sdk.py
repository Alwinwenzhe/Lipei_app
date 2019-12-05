# Author: SH
# Data: 2019/5/26
# Status 
# Comment:

from base.base_driver import BaseDriver

class SysSdk(object):
    '''被测应用中的其它系统activity'''

    def __init__(self,i):
        self.dr = i         # 这里传递进来的就是driver

    def get_sys_pic_activity(self):
        '''
        打印当前activity：这里就是获取系统相册activitry
        :return:
        '''
        pic_act = self.dr.current_activity
        print("activity is:",pic_act)
        return pic_act
