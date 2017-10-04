# -*- coding:utf-8 -*-

#在python操作文件
#打开文件
#基本文件方法
#对文件内容进行迭代

#如果找不到会报错 IO错误
f=open(r'C:\Users\asus\pycharmProjects\python27\abc.txt')
#f=open() #第二个参数如果不给，那么默认是读取 ‘r’
#  ‘r':读模式   'w':写模式   'a':追加模式  'b'：二进制模式  '+'读/写模式

print '01:',f.read()
print '01:',f.read() #指针到了末尾 所以读出来空的

f=open(r'C:\Users\asus\pycharmProjects\python27\abc.txt')
print '02:',f.read(5)  #读取了5个字符
f.seek(5)   #移动指针
print '03:',f.read(3)
f.seek(0)   #移动指针
print '03:',f.read(5)

f.seek(0)
print '04:',f.readline()
print '04:',f.readline()
print '04:',f.readline()

f.seek(0)
print '05:',f.readlines()

#关闭文件
f.close()



#文件写入
fw=open(r'C:\Users\asus\pycharmProjects\python27\abc.txt','w')
#此时不能调用read函数
fw.write('python write txt')
fw.write('1234567')
fw.close()
#追加模式
fa=open(r'C:\Users\asus\pycharmProjects\python27\abc.txt','a')
fa.writelines(['fa mode write','2 line'])
fa.close()

#实例     windows下换行就是\r\n
f2=open(r'C:\Users\asus\pycharmProjects\python27\aaaa.txt','r')
list2=f2.readlines()
print list2
f2.close()
list2[1]="isn't a \n"
list2.append('\n1234567\n')
f2=open(r'C:\Users\asus\pycharmProjects\python27\aaaa.txt','w')
f2.writelines(list2)
f2.close()

#对文件内容进行迭代
f8=open(r'C:\Users\asus\pycharmProjects\python27\ddd.txt')
char=f8.read(1)

def process(c):
    print '00:',c
#一次读一个字符   #另外一种写法   #for char in f.read():
while char:
    process(char)
    char=f8.read(1)

while True:
    char=f8.read(1)
    if not char:break
    process(char)
f8.close()



#一次读一行    # for line in  f.readlines():
def process(c):
    print '11:', c
f9 = open(r'C:\Users\asus\pycharmProjects\python27\ddd.txt')
while True:
    line = f9.readline()
    if not line: break
    process(line)
f9.close()

#文件的写法
fw=open(r'C:\Users\asus\pycharmProjects\python27\ccc.txt','w')
fw.write('First line\n')
fw.write('secon line\n')
fw.write('third line\n')
fw.close()
lines=list(open(r'C:\Users\asus\pycharmProjects\python27\ccc.txt'))
print lines

first,second,third=open(r'C:\Users\asus\pycharmProjects\python27\ccc.txt')
print '1123:',first,second,third

