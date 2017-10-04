# -*- coding:utf-8 -*-
#python生成器

#什么是生成器： 是一种函数，一个（利用yield语句）产生序列的函数，生成一个序列的值，就是一种用普通函数语法定义的迭代器
#创建生成器
#递归生成器
#通用生成器
#生成器方法
#模拟生成器


#创建生成器
nested=[[1,2,3],[4,5],[6,7]]
def flattend(ns):  #这个函数就是一个生成器
    for sublist in ns:
        for element in sublist:
            yield element
for num in flattend(nested):
    print num

print list(flattend(nested))

#生成器表达式
g=((i+2)**2 for i in range(2,27))  #这种情况生成器表达式需要加小括号
print g.next()
print list(g)
print sum(i**2 for i in range(10))  #这种情况生成器表达式不需要加小括号


#生成器中使用递归

def flattend(ns):#带递归方式的生成器
    try:
        for sublist in ns:
            for element in flattend(sublist):
                yield element
    except TypeError:
        yield ns

print list(flattend([[[1,2,[9,2],8,9,10],2,3,5,9],10]))

def flatted(ns):  #字符串序列的生成器
    try:
        try:
            ns+''
        except TypeError:pass
        else:
            raise TypeError
        for sublist in ns:
            for element in flatted(sublist):
                yield element
    except TypeError:
        yield ns

print list(flatted(['foo',['bar',['baz']]]))


#生成器方法 send()
def repeater(value):
    while True:
        new=(yield value)
        if new is not None:value=new

r=repeater(42)
print r.next()
print r.send("Hello World!")

#模拟生成器  python以前的写法
def flatted2(nested):
    result=[]
    try:
        try:
            nested+''
        except TypeError:pass
        else: raise TypeError
        for sublist in nested:
            for element in flatted2(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result


print flatted2(['foo','c',['bar',['baz']]])

