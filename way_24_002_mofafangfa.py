# -*- coding:utf-8 -*-
__metaclass__=type

class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print "Aaaah..."
            self.hungry=False
        else:
            print "No,thanks!"

class SongBird(Bird):
    def __init__(self):
        self.sound='Squawk!'
    def sing(self):
        print self.sound

sb=SongBird()
sb.sing()
# sb.eat()  #产生错误因为父类的构造方法已经被重写了，为了避免这种错误，两种方式可以解决

#第一种解决方法，旧版
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print "Aaaah..."
            self.hungry=False
        else:
            print "No,thanks!"

class SongBird(Bird):
    def __init__(self):
        #调用未绑定的超类构造方法
        Bird.__init__(self)
        self.sound='Squawk!'
    def sing(self):
        print self.sound

sb = SongBird()
sb.sing()
sb.eat()


#第二中解决方法，新版，用super函数只能在新式类中使用
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print "Aaaah..."
            self.hungry=False
        else:
            print "No,thanks!"

class SongBird(Bird):
    def __init__(self):
        #新式类中使用super函数
        super(SongBird,self).__init__()#新式类的调用父类构造方法
        self.sound='Squawk!'
    def sing(self):
        print self.sound

sb = SongBird()
sb.sing()
sb.eat()

