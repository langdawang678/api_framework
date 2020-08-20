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
        # 登录

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_recharge(self, test_data):
        pass


# 运行的时候一定要注意右键的位置，否则会出现奇怪的报错
if __name__ == '__main__':
    unittest.run()
