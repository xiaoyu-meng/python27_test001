# -*- coding:utf-8 -*-

#random 模块 随机数模块 产生随机数
#shelve模块 架子模块

from random import *
#random()返回0-1的随机小数
print "01:",random()
print "02:",random()

#getrandbits(n)    返回随机长整型数  长度由n指定，n是二进制
print "03:",getrandbits(32)
print "03:",getrandbits(8)
print "03:",getrandbits(16)

#uniform(a,b)  返回a=<  <b之间的实数
from time import *
date1=(2008,1,1,0,0,0,-1,-1,-1)
date2=(2009,1,1,0,0,0,-1,-1,-1)
time1=mktime(date1)
time2=mktime(date2)
random_time=uniform(time1,time2)
print "04:",random_time
print "05:",asctime(localtime(random_time))

# randrange() 一个参数代表返回0-参数的数据，  也可以指定开始  结尾 步长
num=3
sides=6
sum1=0
for i in range(num):
    sum1+=randrange(1,7,1)
print "06:",sum1

num=3
sides=6
sum1=0
for i in range(num):
    sum1+=randrange(6)+1
print "06:",sum1


#sides.py
#一个投掷骰子的小游戏
# from random import *
# num=input('How many dice?')
# sides=input("How many sides per die?")
# sum=0
# for i in range(num):
#     sum+=randrange(sides)+1
# print 'The result is ',sum

# choice(seq)  返回后面序列中的随机一个字符
print "07:",choice(["abc","ttt","eee","sdfs","123",'ppp'])
s=["abc","ttt","eee","sdfs","123",'ppp']
#打乱顺序
print "08:",s
shuffle(s)
print "08:",s

#在序列中随机返回n个元素  sample()
print "09:",sample(s,3)  #随机返回序列中的三个数据


#实例  发扑克牌
# from pprint import pprint
# value=range(1,11)+('J Q K').split()
# print "10:", value
# suits="diamonds clubs hearts spades".split()
# print "10:", suits
# deck=['%s of %s' % (v,s) for v in value for s in suits]
# print "10:", deck[:20]
# pprint(deck[:12])
#
# shuffle(deck)
# pprint(deck[:12])
# while deck:
#     raw_input(deck.pop())  #敲一次回车  发一次排



#架子模块  在硬盘上用字典方式存储
import shelve
s=shelve.open("test.dat")
s["x"]=["a",'b','c']
print "12:",s
s["x"].append('d')
print "12:",s

temp=s['x']
temp.append('d')
s['x']=temp
print "12:",s

#模拟一个数据库小程序

#database.py
import sys,shelve
def store_person(db):
    """
    Quer y user for data and store it in the shelf objece
    """
    pid=raw_input("Enter your ID number:")
    person={}
    person['name']=raw_input("Enter your name:")
    person["age"]=raw_input("Enter age:")
    person["phone"]=raw_input("Enter phone number")
    db[pid]=person
def lookup_person(db):
    """
    Query user for ID and desired field,and fetch the corresponding data from the shelf object
    """
    pid=raw_input('Enter ID number:')
    field=raw_input("What would you like to know ?(name,age,phone)")
    field=field.strip().lower()
    print field.capitalize()+":",db[pid][field]
def print_help():
    print "The available commands are:"
    print "store : stores information about a person"
    print 'lookup :Looks up a person from ID number'
    print "?      :Print s this message"
def enter_command():
    cmd=raw_input("Enter command(? for help):")
    cmd=cmd.strip().lower()
    return cmd
def main():
    database=shelve.open("D:\\database.dat")
    try:
        while True:
            cmd=enter_command()
            if cmd=="store":
                store_person(database)
            elif cmd=="lookup":
                lookup_person(database)
            elif cmd=="?":
                print_help()
            elif cmd=="quit":
                return    #跳出
    finally:
        database.close()

if __name__=="__main__":
    main()




