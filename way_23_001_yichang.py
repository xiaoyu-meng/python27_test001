# -*- coding:utf-8 -*-

#什么是异常  ，异常就是非正常运行
#捕捉异常
#多个except语句
#一个块捕捉多个异常
#捕捉对象
#真正的全捕捉
#else子句
#finally子句
#函数中加异常处理



# raise Exception  #引发异常

# 10/0

# raise Exception（"hyperdrive overload"）


#python 内建异常

#Exception 所有异常的基类
#AttributeError 特性引用或赋值失败时引发
#IOError 试图打开不存在的文件时引发
#IndexError 在使用序列中不存在的索引时引发
#KeyError 在使用映射中不存在的键时引发
#NameError 在找不到名字（变量）时引发
#SyntaxError 在代码为错误形式时引发
#TypeError 在内建操作或函数应用于错误类型的对象时引发
#ValueError 在内建操作或者函数应用于正确类型的对象，但是该对象使用不合适的值时引发。
#ZeroDivisionError 在除法或者模除操作的第二个参数为0时引发

# class SomeCustomException(Exception):pass
# raise SomeCustomException("sssss")


#捕捉异常#try 语句
# x=input("Please enter the first number")
# y=input("Please enter the second number")
# print x/y
#这个程序本身没有问题，但是如果用户输入y=0,那么程序就会有异常，这种情况下需要捕捉异常
# try:
#     x = input("Please enter the first number")
#     y = input("Please enter the second number")
#     print x / y
# except ZeroDivisionError:
#       print "The second number can't be zero"

# class MuffledCalculator:
#     muffled=False
#     def calc(self,expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print "Division by zero is illegal"
#             else:
#                 raise
#
# calculator=MuffledCalculator()
# calculator.calc('10/2')
# # calculator.calc('10/0')
#
# calculator.muffled=True
# calculator.calc('10/0')

#try:
#    可能会引发异常的代码
#except ZeroDivisionError:
#     print ""
#except TypeError:
#     print ""

# try:
#     x = input("Please enter the first number")
#     y = input("Please enter the second number")
#     print x / y
# except ZeroDivisionError:
#     print "The second number can't be zero"
# except NameError:
#     print "变量名错误"
# except TypeError:
#     print "请输入数字"

# try:
#     x = input("Please enter the first number")
#     y = input("Please enter the second number")
#     print x / y
# except ZeroDivisionError,e:
#     print "The second number can't be zero",e
# except NameError,e2:
#     print "变量名错误",e2
# except TypeError,e3:
#     print "类型异常，请输入数字",e3


#任何错误都捕获到一个except里面
# try:
#     x = input("Please enter the first number")
#     y = input("Please enter the second number")
#     print x / y
# except :
#     print "出错"
#
# try:
#     x = input("Please enter the first number")
#     y = input("Please enter the second number")
#     print x / y
# except (ZeroDivisionError,NameError,TypeError):
#     print "可能发生三种异常情况"
#
# try:
#     x = input("Please enter the first number")
#     y = input("Please enter the second number")
#     print x / y
# except (ZeroDivisionError,NameError,TypeError),e:
#     print "可能发生三种异常情况:",e



#else 语句 finally语句

# #try语句块正常执行完毕之后,，没有异常，就会执行else语句
# while True:
#     try:
#         x=input("Enter the first number:")
#         y=input("Enter the second number:")
#         value=x/y
#         print  'x/y is ',value
#     except Exception,e:
#         print "Invalid input" ,e
#         print "Please try again"
#     else:
#         break


#无论try是否捕获到异常，finally语句都会执行。
# x=None
# try:
#     x=1/0
# finally:
#     print "Cleaning up..."
#     del x

#
# #try语句不可以单独存在，except else finally都是可有可无。
# try:
#     x=1/0
# except:
#     print "出错了"
# else:
#     print "执行else子句"
# finally:
#     print "这是fianally子句"

#函数中处理异常
def faulty():
    raise Exception("Something is wrong")
def ignore_exception():
    faulty()
def handle_exception():
    try:
        faulty()
    except:
        print "Exception handled"

# ignore_exception()
# handle_exception()

