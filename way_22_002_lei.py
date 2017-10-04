# -*- coding:utf-8 -*-

__metaclass__=type   #指定新式类的语句

class Person:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello,world! I'm %s" % self.name



foo=Person()
bar=Person()
foo.setName("Luke skywalker")
bar.setName("Anakin Skywalker")
foo.greet()
bar.greet()

print foo.name
print bar.name


class Class:
    def method(self):
        print "I have a self"
def function():
    print "I don't ...."

instance=Class()
instance.method()
instance.method=function  #注意写的形式
instance.method()