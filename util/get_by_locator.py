# Author: SH
# Data: 2019/5/16
# Status 
# Comment:

from .oper_ini import OperIni
from appium.webdriver.common.mobileby import By

class GetByLocator(object):
    '''
    将ini中value转化为定位类型及值，并将值返回
    '''
    def __init__(self,driver):
        self.oi = OperIni()
        self.driver = driver

    def get_locator(self,partition,key):
        '''
        注意这里的定位元素不带elements
        :param partition:
        :param key:
        :return:
        '''
        locator = self.oi.read(partition,key)
        if locator != None:
            by_way,ele = locator.split(">")
            if by_way == 'id':
                return self.driver.find_element(by=By.ID,value=ele)
            elif by_way == 'class':
                return self.driver.find_element(by=By.CLASS_NAME, value=ele)
            elif by_way == 'xpath':
                return self.driver.find_element(by=By.XPATH, value=ele)
            elif by_way == 'css':
                return self.driver.find_element(by=By.CSS_SELECTOR, value=ele)
            elif by_way == 'text':
                return self.driver.find_element(by=By.LINK_TEXT, value=ele)
            elif by_way == 'par_text':
                return self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=ele)
            elif by_way == 'ui_text':
                return self.driver.find_element_by_android_uiautomator(('new UiSelector().text({0})'.format(ele)))
            elif by_way == 'ui_id':
                return self.driver.find_element_by_android_uiautomator(('new UiSelector().resource-id({0})'.format(ele)))
            else:
                return None
                print("\033[1;33mini中定位方式不匹配，请检查\033[0m")

    def get_locators(self,partition,key):
        '''
        注意这里的定位元素不带elements
        :param partition:
        :param key:
        :return:
        '''
        locator = self.oi.read(partition,key)
        if locator != None:
            by_way,ele = locator.split(">")
            try:
                if by_way == 'id':
                    return self.driver.find_elements(by=By.ID,value=ele)
                elif by_way == 'class':
                    return self.driver.find_elements(by=By.CLASS_NAME, value=ele)
                elif by_way == 'xpath':
                    return self.driver.find_elements(by=By.XPATH, value=ele)
                elif by_way == 'css':
                    return self.driver.find_elements(by=By.CSS_SELECTOR, value=ele)
                elif by_way == 'text':
                    return self.driver.find_elements(by=By.LINK_TEXT, value=ele)
                elif by_way == 'par_text':
                    return self.driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=ele)
                elif by_way == 'ui_text':
                    return self.driver.find_elements_by_android_uiautomator(('new UiSelector().text({0})'.format(ele)))
                else:
                # elif by_way == 'ui_id' 调试try，注销本行:
                    return self.driver.find_elements_by_android_uiautomator(('new UiSelector().resource-id({0})'.format(ele)))
            except:    #识别到不同的类型了
                self.driver.save_screenshot(r"D:\Job\python\Script\Lipei_app\report\error_pic\err.jpg")     #这里写入图片失败
                return None
                print("\033[1;33mini中定位方式不匹配，请检查\033[0m")
        else:
            return None