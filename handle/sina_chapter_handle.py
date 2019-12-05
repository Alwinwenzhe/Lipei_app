# Author: SH
# Data: 2019/5/17
# Status 
# Comment:

from page.sina_chapter import SinaChapter
import time
from handle.sys_sdk import SysSdk
from business.sina_choose_pics_business import SinaChoosePicsBusiness

class SinaChapterHandle(object):
    '''
    文章页面业务处理
    '''
    def __init__(self,driver):
        self.ch = SinaChapter(driver)
        self.ss = SysSdk(driver)
        self.dr = driver
        self.cp = SinaChoosePicsBusiness(driver)

    def input_title(self,title):
        '''
        输入文章title
        :param title:
        :return:
        '''
        edit_activity = self.ss.get_sys_pic_activity()
        print(edit_activity)
        self.ch.title().clear()
        self.ch.title().send_keys(title)
        time.sleep(6)

    def input_content(self,content):
        '''
        输入文章content
        :param content:
        :return:
        '''
        self.ch.content().clear()
        self.ch.content().send_keys(content)
        time.sleep(2)

    def click_next(self):
        '''
        點擊下一步
        :return:
        '''
        self.ch.next().click()

    def save_chapter(self):
        '''
        保存文章内容
        :return:
        '''
        self.ch.save().click()

    def send_chapter(self):
        '''
        發送文章到首页
        :return:
        '''
        self.ch.chapter_send().click()

    def click_pic(self):
        '''
        点击图片按钮
        :return:
        '''
        self.ch.pic().click()

    def choose_pic(self,activity):
        '''
        选择相片
        :return:
        '''
        self.dr.wait_activity(activity,30,3)
        # self.dr.tap([(407,83),(619,156)],500)    # 通过uiautomator的bounds实现，亲测可行
        self.cp.choose_pics()