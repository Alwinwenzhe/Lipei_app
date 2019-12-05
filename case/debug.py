# Author: SH
# Data: 2019/5/16
# Status 
# Comment:
import sys, os


li = [1,2,3,4,5,6,7,8,9]
print(type(li),li)
print ([x**2 for x in li])   # x循环取出列表值，并2次幂

print ([x**2 for x in li if x>5])       # x循环取出列表值，当值大于5进行2次幂运算

print (dict([(x,x*10) for x in li]))  #x循环取出列表值当作key，并且乘10得到的值当value，封装为字典；注意这里是强制转化所以用括号

print  ([ (x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8 ])
# x从1到9循环，并且x除2的摩大于0且x大于3和对应y的取值形成值对

print ([x*y for x in ([1,2,3]) for y in  (1,2,3)])

testList = ([1,2,3,4])
def mul2(x):
    return x*2
print ([mul2(i) for i in testList])

