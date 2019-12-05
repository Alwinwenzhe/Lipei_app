# Author: SH
# Data: 2019/5/26
# Status 
# Comment:
from page.sina_photo_album import SinaPhotoAlbum
import time

class SinaPhotoAlbumHandle(object):

    def __init__(self,driver):
        self.sp = SinaPhotoAlbum(driver)

    def click_photo_album(self):
        '''
        点击相册选择
        :return:
        '''
        self.sp.choose_photo_album().click()

    def choose_photo_album(self):
        '''
        选择相册
        :return:
        '''
        self.sp.choose_pic().click()
        time.sleep(3)

    def choose_pics(self):
        '''
        选择多个照片
        :return:
        '''
        pics = self.sp.choose_pics()
        for i in pics:
            time.sleep(1)
            i.click()

    def next(self):
        '''
        点击下一步
        :return:
        '''
        self.sp.next().click()
