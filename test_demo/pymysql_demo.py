'''
接口base_url：http://120.78.128.25:8766/futureloan
mysql数据库连接信息：
120.78.128.25
3306
future
123456
'''

import pymysql
from pymysql.cursors import DictCursor

# 建立连接
conn = pymysql.connect(
    host='120.78.128.25',
    port=3306,
    user='future',
    password='123456',
    charset='utf8',  # 不是utf-8
    database='futureloan',
	cursorclass=DictCursor   #
)
# print(conn)  # <pymysql.connections.Connection object at 0x7ffd54fd6b50>

# 游标(光标)
cursor = conn.cursor()  # 游标类

# 执行sql语句
cursor.execute("SELECT * FROM member LIMIT 2;")


mobile ="13712341234"
# 传递参数的方式1：format，不推荐，会有sql注入风险
# cursor.execute('select * from member where mobile_phone={};'.format(mobile))
# 方式2： args 参数  %s ，sql的占坑符号，不同于字符串的%
cursor.execute('select * from member where mobile_phone=%s;', args=[mobile, ])


# 获取游标结果
one = cursor.fetchone()
all = cursor.fetchall()  # 共用一个游标，导致获取到的数据往后移

print(one)  # 没有cursorclass=DictCursor，则类型为元组。加上为字典，方便查询。


# 关闭，避免造成内存消耗
cursor.close()
conn.close()





