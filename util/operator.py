# Author: SH
# Data: 2019/5/9
# Status 
# Comment:

from appium import webdriver
from time import sleep

class Operator(object):
    '''
    主要是手机上各种操作姿势的封装
    '''
    def get_driver(self):
        capabilities ={
            "platformName": "Android",
            "unicodeKeyboard": 'true',
            "deviceName": "3XU9X17324W10646",
            "noReset": 'true',
            "platformVersion": "6.0",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.SplashBadgeActivity"       #appium1.7版本之后就应该不需要改配置了
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
        sleep(8)
        return driver
        # 对应的cmd中需先执行：appium -p 4723 -bp 4724 -U 3XU9X17324W10646

    #获取屏幕宽高
    def get_size(self):
        size = driver.get_window_size()
        width = size['width']
        height = size['height']
        return width,height

    #向左滑动：
    def swip_left(self):
      """
      此方法适合在顶部banner位置进行滑动
      :return:
      """
      x = self.get_size()[0]/10*9
      y = self.get_size()[1]/10*2
      x1 = self.get_size()[0]/10*4
      driver.swipe(x,y,x1,y)

    def swip_right(self):
      x = self.get_size()[0] / 10 * 1
      y = self.get_size()[1] / 10 * 2
      x1 = self.get_size()[0] / 10 * 9
      driver.swipe(x,y,x1,y)

    def swip_up(self):
      '''
      此方法是从底部往上滑动
      :return:
      '''
      x = self.get_size()[0] / 10 * 1
      y = self.get_size()[1] / 10 * 8
      y1 = self.get_size()[1] / 10 * 4
      driver.swipe(x,y,x,y1)

    def swip_down(self,driver):
      '''
      向下滑动
      :return:
      '''
      x = self.get_size()[0] / 10 * 2
      y = self.get_size()[1] / 10 * 2
      y1 = self.get_size()[1] / 10 * 7
      driver.swipe(x,y,x,y1)

    def swip_on(self,direction):
        '''
        再次封装4个滑动方法:up,down,left,right
        :return:
        '''
        if direction == 'up':
            self.swip_up()
        elif direction == 'down':
            self.swip_down()
        elif direction == 'left':
            self.swip_left()
        elif direction == 'right':
            self.swip_right()
        else:
            print('noting swip!!!')

if __name__ == '__main__':
    driver = Operator()
    driver.swip_on("left")
    print('reset 3 seconds:-------')
    sleep(3)            #这里不等待时间很有可能两个滑动至生效一个
    driver.swip_on("left")
    print('reset 3 seconds:-------')