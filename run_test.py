import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

from config.setting import config

testloader = unittest.TestLoader()
suite = testloader.discover(config.case_path)

# 测试报告
ts = str(int(time.time()))
file_name = "test_result_{}.html".format(ts)
file_path = os.path.join(config.report_path, file_name)


with open(file_path, "wb") as f:
    # runner = HTMLTestRunner(f,
    #                         title="前程贷接口测试报告-title",
    #                         description="前程贷接口测试报告-description",
    #                         tester="zhangsan")
    runner = HTMLTestRunner(f,
                            title="前程贷接口测试报告-title",
                            description="前程贷接口测试报告-description")
    runner.run(suite)
