import json
import unittest
import ddt

from common.openpyxl_handle import ExcelHandler
from common.requests_handler import RequestsHandler
from config.setting import config


@ddt.ddt
class TestRegister(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.get_all("register")

    def setUp(self) -> None:
        self.req = RequestsHandler()
        # 这里要加括号，表名是实例化的对象，否则是类的调用
        # req要加self，其他方法要调用

    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*data)
    def test_register(self, test_data):
        # def visit(self, url, method, params=None, data=None, json=None, **kwargs):
        res = self.req.visit(config.host + test_data["url"],
                             test_data["method"],
                             json=json.loads(test_data["json"]),
                             # excel读取的是str（json字符串），需要转为dict（json格式）
                             headers=json.loads(test_data["headers"]))

        self.assertEqual(test_data["expected"], res["code"])

        # 把实际结果写入excel。 实际不太用得到，因为输出到测试报告中了。
