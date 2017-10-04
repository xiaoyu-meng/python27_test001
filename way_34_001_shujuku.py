# -*- coding:utf-8  -*-

#  Oracle  SQL Server
#掌握python与数据库连接的方式
#python数据库API
#全局变量
#连接和游标
#异常
#SQLite数据库应用程序示例

#DB-API规范

import sqlite3
print '01:',sqlite3.apilevel
print '02:',sqlite3.threadsafety
print '03:',sqlite3.paramstyle

# import 数据库模块
# 我的连接=数据库模块.connect()
# 我的连接.query(“sql语句”)
# 我的连接.commit()   #提交
# 我的连接.close()
#
# import 数据库模块
# 连接=数据库模块.connect()
# 游标=连接.coursor()
# 游标.excute(“sql语句”)
# rows=游标.fetchall()
#
# 游标.close()
# 连接.commit()
# 连接.close()

# conn=sqlite3.connect('somedatabase.db')
# curs=conn.cursor()
# conn.commit()
# conn.close()

#实例--------------------------

#创建模块，把数据导入数据库
#importdata.py

import sqlite3

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value='0'
    return float(value)

conn=sqlite3.connect('food.db')
curs=conn.cursor()
curs.execute("""
create table food(
id      text  primary  key,
desc    text,
water   float,
kcal    float,
protein  float,
fat      float,
ash      float,
carbs    float,
fiber    float,
sugar    float
                   )
           """)

query='insert into food values(?,?,?,?,?,?,?,?,?,?)'
for line in open('ABBREV.txt'):
    field=line.split('^')
    value=[covert(f) for f in fields[:10]]
    curs.execute(query,vals)
conn.commit()
conn.close()


#从数据库文件读取
#food_query.py
import sqlite3,sys

conn=sqlite3.connect('food.db')
curs=conn.cursor()

query='select * from food where %s' % sys.argv[1]
print query
curs.execute(query)
names=[f[0] for f in curs.description]
for row in cur.fetchall():
    for pair in zip(names,row):
        print '%s:%s' % pair
    print

