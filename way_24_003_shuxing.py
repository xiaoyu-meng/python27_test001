# -*- coding:utf-8 -*-
__metaclass__=type #新式类指定
#属性：通过隐藏的访问器来访问类下变量的方法叫属性

# 假的
# class Rectangle:
#     def __init__(self):
#         self.width=0
#         self.height=0
#     def setSize(self,size):
#         self.width,self.height=size
#     def getSize(self):
#         return self.width,self.height
#
# r=Rectangle()
# r.width=10
# r.height=5
# print r.getSize()
# r.setSize((150,110))
# print r.getSize()

#正确的
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setsize(self,size):
        self.width, self.height = size
    def getsize(self):
        return self.width,self.height
    size=property(getsize,setsize) #size就是属性，通过封装getsize setsize
r=Rectangle()
r.width=10
r.height=5
print r.size
r.size=(150,100)
print r.size

#拦截的方法
class Rectangle2:
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self, key, value):
        if key=='size':
            self.width,self.height=value
        else:
            self.__dict__[key]=value
    def __getattr__(self, item):
        if item=='size':
            return self.width,self.height
        else:
            raise AttributeError
r2=Rectangle2
r2.size=(120,100)
print r2.size

