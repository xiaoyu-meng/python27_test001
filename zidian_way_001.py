# -*- coding: utf-8 -*-

# 字典 键不能是列表，而且不可以重复，键值可以是列表，可以重复

phonebook={'Alice':'1234','zhangsan':'8754','Cecil':'3258'}
d1 = {'spam':2,"ham":1,'eggs':3}
d2={'food':{'spam':2,"ham":1,'eggs':3}}
d3={}

print phonebook['Alice']

items=[('name','Gumby'),('age',42)]
d=dict(items)
print d
print d['name']
d4=dict(name='Gumby',age=42)
print 'd4:%s'% d4

phonebook['zhangsan']=5555
print phonebook

del phonebook['zhangsan']
print phonebook

print 'Alice' in phonebook
print 'Alices' in phonebook

phonebook['abc'] = 5555
print phonebook

# 字典 字符串的格式化
print "Cecil's phone number is:%(Cecil)s" % phonebook
template='''<html>
          <head><title>%(title)s</title></head>
          <body>
          <h1>%(title)s</h1>
          <p>%(text)s</p>
          </body></html>'''
data={'title':"My Home Page",'text':'Welcome to my home page'}
print template % data

