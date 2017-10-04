# -*- coding:utf-8 -*-

#python 标准库
#集合 堆 双端队列
#time 模块

#set中的数据没有重复 集合
print set(range(10))
print set([0,1,2,8,3,4,5,6,0,1,2,3,4,5,6,7])

#并集 交集
a=set([1,2,3])
b=set([2,3,4])
print a.union(b)  #并集
print a|b   #并集

c=a&b  #交集
print c
print a.intersection(b)  #交集
print '1:',c.issubset(a)  #判断c是不是a的子集
print '1:',c<=a    #判断c是不是a的子集
print '2:',c.issuperset(a)  #判断c是不是a的父集
print '2:',c>=a  #判断c是不是a的父集

#两个集合相减
print '3:',a.difference(b)
print '3:',a-b

#两个的集合的并集减去交集
print '4:',a.symmetric_difference(b)
print '4:',a^b

#拷贝
print a.copy() is a
#集合不能作为字典的键
#集合中的值不可变，集合可变

# a.add(b)# 会出现运行错误
a.add(frozenset(b))#  frozenset  把集合变成一个不可变的集合
print a

#堆  优先队列的一种   python中没有这种数据结构，只是用序列模拟实现
#heapq
from heapq import *
from random import shuffle
data=range(10)
print '1:',data
shuffle(data)
print '2:',data
heap=[]  #堆属性
for n in data:
    heappush(heap,n)    #数据要比他的位置除以2的位置上的数据要大  这种属性称之为堆属性
print heap

#弹出一个数据heappop,弹出最小的数据
print '3:',heappop(heap)
print '4:',heappop(heap)
print '4:',heap

heap=[5,8,9,1,0,3,6,7,9,1,5]
heapify(heap)  #堆属性排序
print '5:',heap

#元素替换
heapreplace(heap,2.8)
print '6:',heap
# heappush()  heappop()  heapify() heapreplcae()
#返回最大的一个元素  nlargest(n,iter)
#返回最小的一个元素 nsmallest(n,iter)

#双端队列
# collections 模块有一中类型 deque类型
from collections import deque
q=deque(range(5))
print '020:',q
q.append(5)
print '021:',q
q.appendleft(6)
print '022:',q
print '023:',q.pop()
print '024:',q.popleft()
print '025:',q

q.rotate(3)   #右边往左边移动，，负数是左边往右边移动
print '026:',q
q.rotate(3)
print '027:',q
q.rotate(-1)
print '027:',q

#time模块
import time
print '028:',time.asctime()  #把时间元祖转换成字符串
print '029:',time.strftime('%Y-%m-%d') #把时间元祖转换成字符串  格式化
t=time.mktime((2008,1,1,0,0,0,-1,-1,-1))
print '030:',t
print '031:',time.localtime(t) #把秒数转换成时间
print '032:',time.asctime(time.localtime(t))
# time.sleep()让解释器休眠多长时间
#strptime()  把字符串解释成时间元组
#time() 获取系统时间
#strftime 格式华
print '033:',time.strptime('Tue Jan 01 00:00:00 2008','%a %b %d %H:%M:%S %Y')


