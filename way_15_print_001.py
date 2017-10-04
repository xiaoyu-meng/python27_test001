# -*- coding:utf-8 -*-
# python 赋值语句print   import

print 'Hello'
print 'Hello',"World!"

name='Gumby'
salutation='Mr.'
greeting = 'Hello.'
print greeting,salutation,name

print [1,2,3,4]
print (1,2,3)

import math
print math.sqrt(888)

from math import sqrt,floor,pow,sin

print sqrt(4)
print floor(100.23)
print pow(2,3)

from math import sqrt as kp

print kp(121)

import math as fba
print fba.pow(10,2)

# 元组赋值

x,y,z=(1,2,3)
print x,y,z
x,y,z=4,5,6    #不对应会引发错误
print x,y,z

[c,d]=['abc','efg']
print c,d

a,b,c,d='spam'
print a,b,c,d

scoundrel={'name':'Robin','girlfriend':'Marion'}
key,value=scoundrel.popitem()
print key,value

x=y=z=193   #链式赋值  多目标赋值语句
print x,y,z

#增量赋值

x=x+1
y+=1
z-=1

print x,y,z

x*=2
y/=2
print x,y