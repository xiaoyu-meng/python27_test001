# -*- coding:utf-8 -*-

from copy import deepcopy

d={}
d['name']='Gumby'
d['age']=42
print d
d.clear()
print d

#.clear()
x={}
y=x        #=x 这一句将y指向了x的那个变量，对x再次赋值，相当于新建一个值，不会改变y指向的值
x['key']='value'
print '01  x：%s,   y:%s' % (x,y)
x={}
print '02  x：%s,   y:%s' % (x,y)
x={}
y=x        #=x 这一句将y指向了x的那个变量，对x再次赋值，相当于新建一个值，不会改变y指向的值
x.clear()
print '03  x：%s,   y:%s' % (x,y)

x={}
y=x
x={'a':2}
print '04  x：%s,   y:%s' % (x,y)


#.copy()   .remove()

x={'username':'admin','machines':['foo','bar','baz']}
y=x.copy()
print '05  x：%s,   y:%s' % (x,y)
y['username']='mlh'
y['machines'].remove('bar')
print '06  x：%s,     y:%s' % (x,y)

d1={}
d['names']=['Alfred','Bertrand']
c=d.copy()
dc=deepcopy(d)
d['names'].append('Clive')
print c
print dc


# fromkeys


print {}.fromkeys(['name','age'])
print dict.fromkeys(['name','age'])
print dict.fromkeys(['name','age'],[123,'gb'])

#get 方法  haskey

d2={}
print d2.get('name')
print d2.get('name','N/A')
print d2.has_key('name')
d2['name']='Eric'
print d2.has_key('name')

# item  iteriterm

d3={'title':'Python Web Site'}
d3['url']='http://www.python.org'
d3['spam']=0
print '1:%s'% d3
print '2:%s'% (d3.items())
it = d3.iteritems()
print it
print list(it)

print d3.keys()
it1=d3.iterkeys()
print it1
print list(it1)

# pop弹出一个指定键      popitem(弹出最后一个元素，但是字典是没有顺序的，所以是随机的)

d={'x':1,'y':2}
print d
print d.pop("x")
print d

dd={'x':1,'y':2,'z':3,'s':5}
print dd
print dd.popitem()
print dd.popitem()
print dd


# setdefault  设定默认值

s = {}
s.setdefault('name','N/A')
print s

s['name']='Tom'
s.setdefault('name','N/A')
print s

# update

b={'title':'Python Web Site','url':"http://www.python.org",'Changed':'Mar 14 22:19:15 MET  2008'}
print b
x={'title':'Python Language Website'}
b.update(x)
print b


# value     itervalues
b={'title':'Python Web Site','url':"http://www.python.org",'Changed':'Mar 14 22:19:15 MET  2008'}
print b.values()
print b.itervalues()
print list(b.itervalues())
