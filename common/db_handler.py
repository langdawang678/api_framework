
import pymysql
from pymysql.cursors import DictCursor

class DBHandler:
    def __init__(self):
        self.conn = pymysql.connect(
            host='120.78.128.25',
            port=3306,
            user='future',
            password='123456',
            charset='utf8',  # 不是utf-8
            database='futureloan',
            cursorclass=DictCursor  #
        )
        self.cursor = self.conn.cursor()  # 游标类

    def query(self, sql, args=None, one=True):
        self.cursor.execute(sql, args)
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

