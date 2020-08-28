#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2020/8/20 8:22 下午
# @author：langdawang678
import json
import unittest
import ddt
import yaml

from common.db_handler import DBHandler
from common.helper import generate_mobile
from common.logger_handler import LoggerHandler
from common.openpyxl_handle import ExcelHandler
from common.requests_handler import RequestsHandler
from config.setting import config

# yaml读取
from middleware.helper import save_token, Context

f = open(config.yaml_config_path, encoding="utf-8")
#
yaml_data = yaml.load(f, Loader=yaml.FullLoader)


@ddt.ddt
class TestRecharge(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.get_all("recharge")

    logger = LoggerHandler(name=yaml_data["logger"]["name"],
                           level=yaml_data["logger"]["level"],
                           file=yaml_data["logger"]["file"])

    def setUp(self) -> None:
        self.req = RequestsHandler()
        # 这里要加括号，表名是实例化的对象，否则是类的调用
        # req要加self，其他方法要调用

        self.db = DBHandler(host=yaml_data['database']['host'],
                            port=yaml_data['database']['port'],
                            user=yaml_data['database']['user'],
                            password=yaml_data['database']['password'],
                            database=yaml_data['database']['database'],
                            charset=yaml_data['database']['charset'])
        # # 登录 结果
        save_token()
        # 这里的值如果要在测试方法中调用，需要加self
        # token = Context.token
        # member_id = Context.member_id

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_recharge(self, test_data):
        """充值接口"""
        print(test_data['case_name'])
        # 1.替换json数据中的member_id
        # 2.访问接口，并assert 返回值
        token = Context.token
        member_id = Context.member_id

        sql = 'SELECT * FROM member WHERE id=%s;'
        user = self.db.query(sql, args=[member_id])
        before_money = user['leave_amount']

        if '#member_id#' in test_data['json']:
            test_data['json'] = test_data['json'].replace('#member_id#', str(member_id))

        headers = json.loads(test_data["headers"])
        headers["Authorization"] = token
        res = self.req.visit(config.host + test_data["url"],
                             test_data["method"],
                             json=json.loads(test_data["json"]),
                             # excel读取的是str（json字符串），需要转为dict（json格式）
                             # headers=json.loads(test_data["headers"]),
                             headers=headers)
        print(res)

        # 校验1，判断是否充值成功
        self.assertEqual(test_data['expected'], res['code'])

        # 校验2：如果成功，则查询数据库，做充值前后的对比
        if res['code'] == 0:
            # money = json.loads((test_data['json']['amount']))  # TypeError: string indices must be integers
            money = json.loads((test_data['json']))['amount']
            sql = 'SELECT * FROM member WHERE id=%s;'
            user = self.db.query(sql, args=[member_id])
            after_money = user['leave_amount']
            self.assertEqual(int(before_money) + int(money), int(after_money))


# 运行的时候一定要注意右键的位置，否则会出现奇怪的报错
if __name__ == '__main__':
    unittest.run()

