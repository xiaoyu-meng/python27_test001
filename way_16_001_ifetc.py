#-*- coding:utf-8 -*-
print '01:',1>0
print '02:',1<0

print '03:',bool(0)
print '04:',bool(1)

print '05:',True==1
print '06:',False==0

print '07:',True+False+42
print '08:',True+False

print '09:',bool("")
print '10:',bool("ss")

print '11:',bool(None)
print '12:',bool([])
print '13:',bool({})
print '14:',bool(8)
print '15:',bool([4])
print '16:',bool({5:2})
# # if 语句
# name = raw_input("What's your name")
# if name.endswith("mby"):
#     print 'Hello,Mr.',name
# elif name.endswith('abc'):
#     print 'Hello,Mr.abc'
# else:
#     print '不匹配'
#
# name1 = raw_input("What's your name")
# if name1.endswith("by"):
#     if name1.startswith("Mr."):
#         print "Hello Mr.Gumby"
#     elif name1.startswith("Mrs."):
#         print "Hello Mrs.Gumby"
#     else:
#         print "Hello Gumby"
# else:
#     print "Hello Stranger"


x=y=[1,2,3]
z=[1,2,3]
print '20:',x==y
print '21:',x==z
print '22:',x is y
print '23:',x is z
print '24:',x is not y
print '25:',x is not z

print '26:',1 in x
print '27:',10 in z
print '28:',1 not in x

print '30:',"alpha"<"Beta"
print '30:',"alpha">"Beta"

a=89
b=99
c=87
if a>90 and b>=90 and c>=90:
    print "该生是优秀生"
if a>90 or b>=90 or c>=90:
    print "该生是良好学生"
if not c>=90:
    print "c小于90"

#断言
age=10
assert 0<age<100
age=-1
assert 0<age<100,'出错啦，假设错误'       #假设出错