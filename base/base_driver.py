# Author: SH
# Data: 2019/5/19
# Status 
# Comment:
import time
from appium import webdriver
from util.operate_yaml import OperateYaml

class BaseDriver(object):

    def android_driver(self,i):
        '''
        这里的设备名及端口号需要cmd返回，暂时写死
        通过yaml操作获取对应的device及port
        :return:
        '''
        oy = OperateYaml()
        device = oy.get_value('user_info_' + str(i),'deviceName')
        port = oy.get_value('user_info_' + str(i),'p')
        capabilities = {
            "platformName": "Android",
            # "resetKeyboard":"true",
            "unicodeKeyboard": 'true',
            "deviceName": device,
            "noReset": 'true',
            # "platformVersion": "6.0",            # OPPO-a73也可正常运行，所以不需要这个版本号
            "appPackage": "com.sina.weibo",
            "appActivity": "com.sina.weibo.SplashActivity"  # appium1.7版本之后就应该不需要改配置了
        }
        # 对应的cmd中需先执行：appium -p 4723 -bp 4724 -U 3XU9X17324W10646
        driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", capabilities)
        time.sleep(10)

        return driver

    def ios_driver(self):
        pass

    def get_driver(self):
        '''
        处理接入设备是IOS还是安卓，再调用对应方法返回
        :return:
        '''
        pass

    def close_app(self,i):
        '''
        关闭driver
        :return:
        '''
        driver = self.android_driver(i)
        driver.close_app()