# -*- coding:utf-8 -*-

#---类和面向对象
#类和类型
#创建自己的类
#多态  多种形态
#封装  对外部隐藏细节
#继承  避免重复

#类 就是种类  面向对象  一切都是对象  类 就是对象的蓝图
#类型：在python3之后版本类与类型差距越来越小，在2版本中，内建的对象基于类型

print 'abcd'.count('c')
print ['a','b','c','a','e'].count('a')
print ('a','b','f','a').count('a')
#count 是多态行为
print 1+2
print 'a'+'b'
#加好是多态行为

class Secretive:
    def __inaccessible(self):  #不可以直接访问  封装
        print "Bet you can't see me....."
    def accessible(self):
        print "The secret message is :"
        self.__inaccessible()

s=Secretive()
s.accessible()

s._Secretive__inaccessible()   #了解之后 可以调用

class MemberCounter:
    members=0
    def init(self):
        MemberCounter.members+=1

m1=MemberCounter()
m1.init()
print MemberCounter.members
m2=MemberCounter()
m2.init()
print MemberCounter.members

m1.members='Two'  #实例空间下的赋值
print m1.members
print m2.members

#被继承的类叫父类 超类 基类  这个名字是相对的。
#继承的类：叫子类，派生类

class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
class spamFilter(Filter):
    def init(self):
        self.blocked=['spam']

f=Filter()  #类的实例
f.init()
f.filter([1,2,3])
s=spamFilter()
s.init()
print s.filter(['spam','spam','spam','aaa','spam','bbb','ccc'])

print issubclass(spamFilter,Filter)  #1是不是2的子类
print spamFilter.__bases__
#他的父类是谁

#检查实例是不是类的对象
print isinstance(s,spamFilter)
print isinstance(f,spamFilter)

print s.__class__

#多继承

class Calculator:
    def calculate(self,expression):
        self.value=eval(expression)

class Talker:
    def talk(self):
        print "Hi,my value is:",self.value

class TalkingCalculator(Calculator,Talker):
    pass

tc=TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()
