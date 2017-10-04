# -*- coding:utf-8 -*-

#Python魔法方法和属性
#魔法方法是   __something__这种写法，特殊情况下调用
#构造方法
#成员方法
#什么是属性
#属性的创造
#静态方法和类成员方法

#构造方法  在创建实例  对象时候调用的
# class FooBar:
#     def __init__(self):     #构造实例时候自己就调用了
#         self.somevar=42
# f=FooBar()
# print f.somevar
#
# class FooBar:
#     def __init__(self,value=42):     #构造实例时候自己就调用了
#         self.somevar=value
# f=FooBar()
# print f.somevar
# f=FooBar(100)
# print f.somevar
# f=FooBar("This is a constructor argument")
# print f.somevar

#__del__:析构方法   在被回收之前，程序自动调用
#重写方法：对继承的方法，如果觉得不合用，就可以用重写的方式对父类的方法进行覆盖
#对类的构造方法进行重写 看002


#魔法方法的成员方法
#__len__  返回元素数量
#__getitem__(self,key):返回键对应的值
#__setitem__(self,key,value):按照方式存储和key相关的value
#__delitem__(self,key) :删除元素

def checkIndex(key):
    if not isinstance(key,(int,long)):raise TypeError
    if key<0:raise IndexError
class ArithmeticSequence:   #定义一个序列
    def __init__(self,start=0,step=1):
        self.start=start
        self.step=step
        self.changed={}
    def __getitem__(self, key):
        checkIndex(key)
        try:return self.changed[key]
        except KeyError:
            return self.start+key*self.step
    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key]=value
s=ArithmeticSequence(1,2)
print s[4]
s[4]=2
print s[4]

class CounterList(list):
    def __init__(self,*agrs):
        super(CounterList,self).__init__(*agrs)
        self.counter=0
    def __getitem__(self, index):
        self.counter+=1
        return super(CounterList,self).__getitem__(index)

cl=CounterList(range(10))
print cl
cl.reverse()
print cl
del cl[3:6]
print cl
print cl.counter
print cl[4]+cl[2]
print cl.counter


#静态方法 没有self参数，能够被类直接调用定义的时候需要传一个cls的参数
#动态方法类成员方法  能够被类直接调用

class myclass:
    def smeth():  #静态方法
        print "This is 静态方法"
    smeth=staticmethod(smeth)

    def cmeth(cls):
        print "This is 动态方法",cls
    cmeth=classmethod(cmeth)

myclass.smeth()
myclass.cmeth()

#新式写法
class myclass2:
    @staticmethod
    def smeth():  #静态方法
        print "This is 静态方法"
    @classmethod
    def cmeth(cls):
        print "This is 类成员方法",cls
myclass2.smeth()
myclass2.cmeth()



