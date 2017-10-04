# -*- coding:utf-8  -*-

# 什么是模块
#创建模块
#使用模块
#模块的位置
#查看模块的信息


 #程序由模块构成，模块由程序代码（语句）构成
 #一个py文件就是模块
 # import 模块名

#hello.py
print "Hello,world!"


import sys
import pprint
pprint.pprint(sys.path)

import hello

sys.path.append('新的文件路径')  #将新的路径加入python默认搜索路径，再导入就可以了

import copy
print dir(copy)

#列表解析表达式
print [n for n in dir(copy) if not n.startswith('_')]
print copy.__all__
# from copy import *   #这句话就是导入all的所有变量
print help(copy.copy)
print copy.__doc__
print range.__doc__

print copy.__file__