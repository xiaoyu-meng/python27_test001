# -*- coding:utf-8 -*-

#python标准库中的模块
#sys模块：与python解释器相关的信息
#os模块：访问操作系统服务的相关信息模块
#fileinput模块：遍历文本文件的所有行

#sys
import sys
import pprint
print dir(sys)
print sys.path
pprint.pprint(sys.path)
print '01:',sys.argv     #拿到命令行的参数
# print '02:',sys.exit([arg])#用来退出程序

print '03:',sys.modules    #用来返回系统载入的模块  的字典
print '04:',sys.path    #用来路径
print '05:',sys.platform    #显示系统平台
print '06:',sys.stdin    #标准的输入流
print '07:',sys.stdout    #标准的输出流
# print '08:',sys.sterr    #标准的错误流  也是类文件对象


#os模块
import os
os.environ   #对环境变量映射的一个变量
print os.environ['PYTHONPATH']  #取环境变量值

#操作系统的行为，比如打开浏览器
#os.system(r'E:\"Program Files (x86)"\Tencent\QQBrowser\QQBrowser.exe')
#os.startfile(r'E:\Program Files (x86)\Tencent\QQBrowser\QQBrowser.exe')

#更好的打开浏览器的行为
# import webbrowser
# webbrowser.open('https://www.hao123.com')

#os.sep  返回当前系统下的标准的分割符
print '08:',os.sep
#os.pathsep  返回当前系统下的标准的路径分割符
print '09:',os.pathsep
#os.linesep  返回当前系统下的换行分割符
print '10:',os.linesep
print 'aaaaa'+os.linesep+"bbbbb"  #这个代码不管在任何系统下都可以正确换行
#os.urandom(n)  返回加密随机数据


#fileinput模块  遍历文本文件的所有行
#fileinput.input  遍历文本文件的所有行
import fileinput
for line in fileinput.input(r"C:\Users\asus\PycharmProjects\python27\way_020_002_zuoyongyu.py"):
    line=line.rstrip()
    num=fileinput.lineno()
    print '%-60s  # %2i' % (line,num)
#fileinput.filename()    取得当前访问的文件名称
#fileinput.lineno()    取得当前访问的文件的第几行
#fileinput.filelineno()    取得当前访问的文件的总行数
#fileinput.isfirstline()   取得当前访问的文件的是不是第一行
#fileinput.isstdin()   最后一行是否来自标准输入流
#fileinput.nextfile()   文件读取指针移到下一个文件，
#fileinput.close()   关闭当前文件
