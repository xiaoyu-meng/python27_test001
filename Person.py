# -*- coding:utf-8 -*-

__metaclass__=type   #指定新式类的语句

class Person:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello,world! I'm %s" % self.name

