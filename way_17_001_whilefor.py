#-*- coding:utf-8 -*-
# x=1
# while x<=10:
#     print x
#     x+=1

# name="张三"
# while name:
#     name=raw_input("Please enter your name:")
#     print "Hello,%s!" % name



words=["this","is","an","ex","parrot"]
for word in words:
    print word

numbers=[0,1,2,3,4]
for num in numbers:
    print num

#下限包含，上限不包含
print range(0,10,2)
print range(0,10)   #下限包含，上限不包含
print range(15)   #下限包含，上限不包含
print range(100,0,-10)   #前限包含，后限不包含

d={'x':1,'y':2,'z':3}
for key in d:
    print key,'correspond to ',d[key]

for key,value in d.items():
    print key,'correspond to ',value

names=['anne','beth',"george","damon"]
ages=[12,45,32,102]
for i in range(len(names)):
    print names[i],'is',ages[i],"years old"

print zip(names,ages)   #压缩以小长度列表为主
for name,age in zip(names,ages):
    print name,'is',age,"years old"


print zip(range(5),xrange(100))  #压缩以小长度列表为主

strings=['asdfsdfd',"sdfgsdxxx","aaaxxxx","bbbb"]
for string in strings:
    if "xxx" in string:
        index=strings.index(string)
        strings[index]="[censored]"
print strings


strings=['asdfsdfd',"sdfgsdxxx","aaaxxxx","bbbb"]
index=0
for string in strings:
    if "xxx" in string:
        strings[index]="0000000000"
    index+=1
print strings


strings=['asdfsdfd',"sdfgsdxxx","aaaxxxx","bbbb"]
for index,string in enumerate(strings):
    if "xxx" in string:
        strings[index]="5555555"

print strings

print sorted([4,68,95,422,4,5,3,8])
print sorted("Hello,World!")
print list(reversed("Hello,World"))
print ''.join(reversed("Hello,World"))

# from math import sqrt
# for n in range(99,0,-1):
#     root=sqrt(n)
#     if root==int(root):
#         print n,root
#         break

for x in range(0,100):
    if x%2==0:
        continue
    if x%3==0:
        continue
    if x%5==0:
        continue
    if x%7==0:
        continue
    if x%9==0:
        continue
    if x%11==0:
        continue
    print x


# while True:
#     word=raw_input('Please enter a word:')
#     if not word:break
#     print 'The word is:',word

broke_out=False
for x in ['a','b','c','d']:
    if x=='c':
        broke_out=True
        break
if broke_out:
    print "这里是强制退出"
from math import sqrt
for n in range(99,81,-1):
    root=sqrt(n)
    if root==int(root):
        print n
        break
else:     #循环完毕会执行else，跳出循环不执行这个语句
    print "没有找到"


for n in range(99,0,-1):
    root=sqrt(n)
    if root==int(root):
        print n
        break
else:
    print "没有找到"