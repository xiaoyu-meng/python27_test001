# -*- coding:utf-8 -*-

#本地作用域
#全局作用域
#嵌套作用域
#内置作用域


#作用域-命名空间
# LEGB原则：先在本地找变量名，然后嵌套上层寻找，在全局找，最后在内置作用域找
#在不同作用域是可以命名相同变量名字的

# global 语句


x=1
y=2
print vars()

scope=vars()
print scope['x']
print scope['y']

def foo():
    x=42

print x
foo()
print x

def output():
    print '02:',x
output()

def combine(parameter):
    print parameter+external
external='berry'
combine('Shrub')

#global语句
def change_global():
    global x
    x=x+1


print '03:',x
change_global()
print '04:',x

#嵌套作用域
def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor

double = multiplier(2)
print '06:',double(5)

import __builtin__
print dir(__builtin__)