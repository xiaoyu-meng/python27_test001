#-*- coding:utf-8  -*-
#网络编程
#少数几个网络设计模块
#  1  socket模块
#  2 urllib和urllib2模块
#  3 其他模块
#SocketServe 和它的朋友们
#多连接
#Twisted

#socketServer.py
import socket
# host=socket.gethostname() 获取主机名称，得到一个字符串
s=socket.socket() #创建一个服务器套接字对象
port=51234

s.bind(('localhost',port)) #让服务器监听port地址
s.listen(5)    #最多等五个连接
while True:
    c,addr=s.accept()
    print 'Got connection from',addr
    c.send('Thank you for connection')
    c.close()




#客户端代码
#socketClient,py
import socket
s=socket.socket()
s.connect('localhost',51234)
print s.recv(1024)









