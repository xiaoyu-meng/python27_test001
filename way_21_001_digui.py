# -*- coding:utf-8 -*-

#r认识递归
#两个经典的递归实例：阶乘和幂
#递归实例：二元查找

# 递归：引用自身（自己调用自己）要有几本返回值

#原始写法
def factorial(n):
    result=n
    for i in range(1,n):
        result*=i
    return result
print '1:',factorial(6)

#递归写法
def factorial2(n):
    if n==1:
        return 1
    else:
        return n*factorial2(n-1)

print '2:',factorial2(6)
print '3:',factorial2(5)

def power(x,n):
    result = 1
    for i in range(n):
        result*=x
    return result
print '4:',power(3,3)

def power2(x,n):
    if n==0:
        return 1
    else:
        return x*power2(x,n-1)

print '5:',power2(3,5)

#二元查找 二分查找

def search(sequence,number,lower=0,upper=None):
    if upper is None:upper=len(sequence)-1
    if lower==upper:
        assert number==sequence[upper]
        return upper
    else:
        middle=(lower+upper)//2
        if number>sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,middle)
seq=[34,67,8,134,4,100,95]
seq.sort()
print seq
print search(seq,34,0,6)

