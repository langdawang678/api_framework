import pymysql
import yaml
from pymysql.cursors import DictCursor

from config.setting import config


class DBHandler:
    def __init__(self, host, port,
                 user, password,
                 charset, database=None,
                 cursorclass=DictCursor, **kwargs):

        # 初始化：
        self.conn = pymysql.connect(
            host=host, port=port,
            user=user, password=password,
            charset=charset,  # 不是utf-8
            database=database,
            cursorclass=DictCursor, **kwargs  #
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


if __name__ == '__main__':
    # yaml读取
    f = open(config.yaml_config_path, encoding="utf-8")
    #
    yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    db = DBHandler(host=yaml_data['database']['host'],
                   port=yaml_data['database']['port'],
                   user=yaml_data['database']['user'],
                   password=yaml_data['database']['password'],
                   database=yaml_data['database']['database'],
                   charset=yaml_data['database']['charset'])
    res = db.query("select * from member limit 2;", one=False)
    print(res)