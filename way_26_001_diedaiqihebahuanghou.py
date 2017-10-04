# -*- coding:utf-8 -*-

#什么是迭代器
#创建迭代器
#了解八皇后问题
#利用生成器和递归解决八皇后问题

#迭代：重复做一些事情很多次
# 迭代器 1 要有__iter__方法：返回迭代器的方法
#2 还要有 next()方法


class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs=Fibs()
for f in fibs:
    if f>1000:
        print f
        break
fibs=Fibs()
for f in fibs:
    if f>20:
        print f
        break

it = iter([1,2,3,4])
print it.next()
print it.next()
print it.next()
print it.next()#再来一个就超出了

class Testterator:
    value=0
    def next(self):
        self.value+=1
        if self.value>10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti=Testterator()
print list(ti)

#八皇后问题  八个皇后在棋盘上
def conflicat(state,nextX):
    nextY=len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False
def queens(num,state):
    if len(state)==num-1:
        for pos in range(num):
            if not conflicat(state,pos):
                yield pos

print list(queens(4,(1,3,0)))

#以上是四个皇后，下面是八皇后
def conflicat(state,nextX):
    nextY=len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False
def queens(num=8,state=()):
    for pos in range(num):
        if not conflicat(state,pos):
            if len(state)==num-1:
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,)+result

print '4皇后：',list(queens(4))
print '8皇后：',list(queens(8))
i=1
for solution in queens(8):
    print '8皇后：第',i,'次',solution
    i+=1

def prettyprint(s):
    def line(pos,length=len(s)):
        return 'a'*(pos)+'o'+'a'*(length-pos-1)
    for pos in solution:
        print line(pos)

prettyprint((7, 3, 0, 2, 5, 1, 6, 4))

import random
prettyprint(random.choice(list(queens(8))))