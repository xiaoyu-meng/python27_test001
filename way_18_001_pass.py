#-*- coding:utf-8 -*-
# 列表解析式  pass del exec eval
#列表解析式
print '01:',[x*x for x in range(0,10)]

r=[]
for x in range(0,10):
    r.append(x*x)
print '02:',r

result=[]
for x in range(4):
    for y in range(10,14):
        result.append((x,y))
print '03:',result

print '04:',[(x,y) for x in range(4) for y in range(10,14)]

result=[]
for x in range(10):
    if x%2==0:result.append(x)
print '05:',result

print '06:',[x for x in range(10) if x%2==0]

girls=['alice','bernice','clarice']
boys=['chris','arnold','bob']
result=[]
for b in boys:
    for g in girls:
        if b[0]==g[0]:result.append(b+'+'+g)
print '07:',result

print '08:',[b+'+'+g for b in boys for g in girls if b[0]==g[0]]

#del语句
scoundrel={'age':42,'first name':'Robin','last name':'of Locksley'}
robin=scoundrel
print '09:',scoundrel
print '10:',robin
robin['age']=35
print '11:',scoundrel
print '12:',robin
robin=None
del scoundrel
# x=1
# del x
# print '13:',x

x=['Hello','World']
y=x
y[1]='Python'
print '14:',x,y

#exec语句  将字符串变成执行语句

str='print "Hello,world"'
print '15:',str
exec str
exec(str)

scope={}
print '16:',scope.keys()
print '17:',scope.values()
print '18:',len(scope)

# from math import sqrt
# scope={}
# exec 'sqrt=1' in scope
# print '19:',scope.keys()
# print '20:',scope.values()
# print '21:',len(scope)

#eval 求值语句   把字符串当计算的执行语句

# print '22:',eval(raw_input("Enter an arithmetic expression"))
sco={}
sco['x']=22
sco['y']=33
print '23:', eval("(x+y)*2",sco)

sdd={}
exec 'x=100' in sdd
exec 'y=5' in sdd
str='x*y'
print '24:',eval(str,sdd)
