# Author: SH
# Data: 2019/5/26
# Status 
# Comment:
from util.get_by_locator import GetByLocator

class SinaPhotoAlbum(object):
    '''
    相册
    '''
    def __init__(self,driver):
        self.gl = GetByLocator(driver)

    def choose_photo_album(self):
        '''
        相册下拉
        :return:
        '''
        return self.gl.get_locator('sina_photo_album','photoAlbum')

    def choose_pic(self):
        '''
        pic相册
        :return:
        '''
        return self.gl.get_locator('sina_photo_album','pic')

    def choose_pics(self):
        '''
        选择多张照片
        :return:
        '''
        return self.gl.get_locators('sina_photo_album','choose_pics')

    def next(self):
        '''
        下一步
        :return:
        '''
        return self.gl.get_locator('sina_photo_album','next')

