# -*- coding:utf-8  -*-

#re 模块   就是对正则表达式支持的一个模块
#其他标准模块介绍

#正则表达式就是规定文本的格式应该是什么样子的
# 正则表达式  '(http://)?(www\.)?python\.org'

#正则表达式中常见字符和符号

#re模块  compile() 创建模式对象   search() 只在字符串中寻找指定模式，  match（）从开始处匹配对象
#split() 根据匹配模式把字符串拆分开，分割字符串   findall()列出字串中模式所有的匹配项
#sub() 利用表达式的匹配项替换指定的字符串 escape()  转义正则表达式中所用的特殊字符

import re
some_text="alpha,beta,,,,gamma delta"
print '01:',re.split('[, ]+',some_text)
print '01:',re.split('[, ]+',some_text,maxsplit=2)
print '01:',re.split('[, ]+',some_text,maxsplit=1)
pat = '[a-zA-Z]+'
text='"Hm...Err -- are you sure?" he said ,sounding insecure'
print '02:',re.findall(pat,text)
pat2=r'[.?\-\"，]+'
print '03:',re.findall(pat2,text)

#sub函数
pat='{name}'
text = 'Dear {name}'
print '04:',re.sub(pat,"Mr,Gumby",text)

#escape
print '05:',re.escape('www.python.org')
print '05:',re.escape('But where is the ambiguity')

#match     返回一个match object对象
#group(0)    start()  end()   span()
m=re.match(r'www\.(.*)\..{3}','www.python.org')
print '06:',m.group(1)
print '06:',m.group(0)
print '06:',m.start(1)
print '06:',m.end(1)
print '06:',m.span(1)


#实例
#准备两个模版文件  magnus.txt    template.txt
#templates.py
import fileinput,re

field_pat=re.compile(r'\[(.+?)\]')
scope={}
def replacement(match):
    code=match.group(1)
    try:
        return  str(eval(code,scope))
    except SyntaxError:
        exec code in scope
        return ''
lines=[]
for line in fileinput.input():
    lines.append(line)

text=''.join(lines)
print field_pat.sub(replacement,text)

#标准库下其他模块   difflib 比较两个序列的相似程度
#datetime  比time 强大
#itertools 迭代器的模块
#logging 可以让开发人员管理一个或者多个日志文件
#cmd
#查python标准库手册
