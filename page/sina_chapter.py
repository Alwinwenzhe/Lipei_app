# Author: SH
# Data: 2019/5/17
# Status 
# Comment:

from util.get_by_locator import GetByLocator
from base.base_driver import BaseDriver

class SinaChapter(object):
    '''
    新增文章页面元素封装
    '''
    def __init__(self,driver):
        self.driver = driver
        self.gl = GetByLocator(self.driver)

    def title(self):
        '''
        文章标题元素封装
        :return:
        '''
        return self.gl.get_locator('sina_editchapter','title')

    def content(self):
        '''
        文章内容元素封装
        :return:
        '''
        return self.gl.get_locator('sina_editchapter','content')

    def next(self):
        '''
        内容编辑完成后，下一步按钮元素封装
        :return:
        '''
        return self.gl.get_locator('sina_editchapter','next')

    def save(self):
        '''
        文章内容保存按钮元素封装
        :return:
        '''
        return self.gl.get_locator('sina_editchapter','save')

    def chapter_send(self):
        '''
        发布文章按钮元素封装
        :return:
        '''
        return self.gl.get_locator('sina_editchapter','titleSave')

    def pic(self):
        '''
        图片按钮
        :return:
        '''
        return self.gl.get_locator('sina_editchapter','pic')