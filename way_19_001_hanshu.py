# -*- coding:utf-8 -*-
#创建函数 传递参数：参数和共享引用  关键字参数和默认参数  可变参数
#函数是将一些语句集合在一起的代码块 起了名字的代码块
#参数是调用函数时传递的数据
# 返回用 return

def hello(name):  #形参
    return 'Hello, '+name+"!"

print '01: ',hello('zhangsan')
print '02: ',hello('李四')

import math
x=7
print '03: ',math.sqrt(x)

def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-1]+result[-2])
    return result

print '04: ',fibs(11)
print '05: ',fibs(15)

def sq(x):
    '这个函数是求传递数据的平方'
    return x*x
print '06: ',sq(10)
print '07: ',sq.__doc__

#判断一个名称是变量还是函数？

squ=123
print callable(squ)
print callable(sq)

def test():
    print 'This is printed'
    return   #函数到此为止

test()
t=test()
print t

def change1(x):
    x=x+1
    return x
x=100
print change1(x)
print x

def change2(str1):
    str1=str1+str1
    print str1
str5='abc'
print '08: ',change2(str5)
print '09: ',str5

def chang3(n):
    n[0]='Mr. 250'

m=['zhangsan','lisi','wangwu']
print '10: ', m
chang3(m)
print '11: ', m
#   ***列表 字典 传参过程会修改原来的数据

m=['zhangsan','lisi','wangwu']
chang3(m[:])
print '12: ', m

#用分片的方式，就不会修改列表和字典的原值

def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}

storage={}
print '13: ',storage
init(storage)
print '14: ',storage

def lookup(data,label,name):
    return data[label].get(name)

storage['middle']['Lie']='Magnus Lie Hetland'
print '15: ', storage
print '16: ',lookup(storage,'middle','Lie')

def inc(x):return x+1

foo=10
print '17: ',inc(foo)

#指定关键字参数,颠倒位置的方法
print '18: ',lookup(label='middle',data=storage,name='Lie')

#默认参数
def hello_3(greeting='Hello',name='World'):
    print '%s,%s'% (greeting,name)
hello_3()
hello_3('Greeting','universe')

#可变参数        参数的数目不定，用*开头，放到一个元组类型的变量中
def print_params(*params):
    print params

print_params('ab','cd')
print_params(1,2,3,3,3)

#放到字典中 可变参数
def print_params_3(**par):
    print par
print_params_3(x=1,y=2,z=3,abc="ttt")

def print_params_4(x,y,z=3,*pospar,**keypar):
    print x,y,z
    print pospar
    print keypar

print_params_4(1,2,3,5,6,7,8,9,foo=1,bar=2,abc=4)

def add(x,y):return x+y
print add(100,333)
pa=(1,2)
print add(*pa)   #对元组的拆分

params={'name':'Sir Robin','greeting':'years old'}
hello_3(**params)  #将字典拆分

params=(5,)*2
print params

print 125*25
print pow(*params)

a,b=2,3
print a,b