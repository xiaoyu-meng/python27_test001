#-*- coding:utf-8 -*-
people ={
       'Alice':{'phone':'2341','addr':'Foo drive 23'},
       'Beth':{'phone':'9102','addr':'Bar street 42'},
       'Cecil':{'phone':'3158','addr':'Baz avenue 90'}
         }
labels={'phone':'phone number','addr':'address'}
name = raw_input('输入你的名字:')
request=raw_input('Please enter phone number-p or address-a:')
if request=='p':
    key='phone'
if request=='a':
    key='addr'


if name in people:
    print "%s's %s is :%s" % (name,labels[key],people[name][key])