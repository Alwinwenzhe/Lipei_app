## 新浪发布微博

STATUS:PASS    TIME:2019-12-05

特别注意：该代码是针对华为畅享6s调试、新浪微博发布超过10条就会提示发布频繁

####纯python实现app自动化
现阶段：demo能启动app

config中可存放配置文件ini，app元素定位文件yaml(每个yaml为一个单独app或一个yaml包含多个app，都是三级定位)

####问题：
05-14：

头条内容中在数字后输入中文，会显示为：2019&YhBlWXbuUk1ipYADU+qXAImB-100&UUMACg-100&UUNTBVQrgAOL1XnRdu52hGVZZ1CNRGWZTuVTyonGmJGL,k72AApOE3nR-:&YDtSBg-450&UgY-

05-17:
   
   page中的get_tost_element，是否该单独传入driver？？
    
 05-23:
    
  PO模式已完成，可通过excel调用测试数据，但是执行完用例后不能自动结束
  
 2020-04-22：
   
   当新郎微博连续发送5条微博后，第六条提交时，会提示发送频繁---该问题可在运行第5条后，通过执行一定时间段的monkey，每个步骤间隔20s来避免
   