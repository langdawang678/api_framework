import json
import unittest
import ddt
import yaml

from common.logger_handler import LoggerHandler
from common.openpyxl_handle import ExcelHandler
from common.requests_handler import RequestsHandler
from config.setting import config

# yaml读取
f = open(config.yaml_config_path, encoding="utf-8")
#
yaml_data = yaml.load(f, Loader=yaml.FullLoader)


@ddt.ddt
class TestRegister(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.get_all("register")

    logger = LoggerHandler(name=yaml_data["logger"]["name"],
                           level=yaml_data["logger"]["level"],
                           file=yaml_data["logger"]["file"])

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
        try:
            self.assertEqual(test_data["expected"], res["code"])
            # 把实际结果写入excel。 实际不太用得到，因为输出到测试报告中了。
            self.excel_handler.write2(config.data_path,
                                      'register',
                                      test_data['case_id']+1,
                                      9,
                                      "测试通过")

        except AssertionError as e:
            # 记录logger
            self.logger.error(f"测试用例执行失败{e}")
            self.excel_handler.write2(config.data_path,
                                      'register',
                                      test_data['case_id'] + 1,
                                      9,
                                      "测试失败")
            # 捕获异常后，一定要抛出，否则用例是pass的
            raise e

# 运行的时候一定要注意右键的位置，否则会出现奇怪的报错
if __name__ == '__main__':
    unittest.run()