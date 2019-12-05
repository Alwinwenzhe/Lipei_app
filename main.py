# Author: SH
# Data: 2019/5/23
# Status：PASS
# Comment:

import unittest, os, time, sys
import HTMLTestRunner
sys.path.append(r"D:\Job\python\Script\Lipei_app")
import threading, multiprocessing
from business.sina_send_chapter_business import SinaSendChapterBusiness
from base.server import Server
from util.devices import Devices

class ParamTestCase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=None):
        super(ParamTestCase,self).__init__(methodName)      #继承原有的构造方法
        global parames          #定义为全局才能传递给setupclass
        parames = parame

class TestMain(ParamTestCase):
    @classmethod
    def setUpClass(cls):
        print("This is a setupclass,本方法仅执行一次",parames)
        cls.sscb = SinaSendChapterBusiness(parames)

    def setUp(self):
        print("This is a setup,本方法在每个用例执行前执行，多个用例则会执行多次")

    @unittest.skip("test")
    def test_001(self):
        a = 1
        c = 1
        self.assertEqual(a, c, 'ac值不相等')  # 如果该用例执行失败，并不会影响case2的执行

    def test_002(self):
        print("再test_003中打印parame：",parames)
        self.sscb.circl_send_sina()

    def tearDown(self):
        # ser = Server()
        #ser.close_driver(parames)
        print("This is a tearDown,本方法在每个用例执行后执行，多个用例则会执行多次")
        if sys.exc_info()[0]:       #自动捕获所有异常及报错
            self.sscb.driver.get_screenshot_as_file(r"D:\Job\python\Script\Lipei_app\report\error_pic\err.jpg")

    @classmethod
    def tearDownClass(cls):
        ser = Server()
        ser.close_driver(parames)
        time.sleep(1)
        # cls.set_input()
        print("This is a tearDownClass,本方法仅执行一次")

def appium_init():
    server = Server()
    server.appium_start()

def get_suite(i):           #注意这个方式是class之外
    print("get_suite里面的", i)
    suite = unittest.TestSuite()
    suite.addTest(TestMain("test_002",parame=i))            #这里的i会传递给ParamTestCase，由他再传递给TestMain中的setupclass（因为这里是所有用i的起点）
    # file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../report/report.html'))
    html_file = r"D:\Job\python\Script\Lipei_app\report\report_" + str(i) + ".html"
    # now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    with open(html_file, "wb") as fp:
        HTMLTestRunner.HTMLTestRunner(stream=fp, title='示例测试报告', description='执行人：Alwin').run(suite)

def get_devices():
    '''
    返回设备个数
    :return:
    '''
    dev = Devices()
    return len(dev.get_devices())

if __name__ == '__main__':

    appium_init()     #首先启动appium服务
    time.sleep(20)      #appium等待时间
    threads = []
    for i in range (get_devices()):       #这里的多线程被固定为1个了，可以根据device_list来动态调整
        t = multiprocessing.Process(target=get_suite,args=(i,))        #i先传递给get_suite中的addtest中的i
        threads.append(t)
    for j in threads:
        j.start()


