import os


class Config:
    # 项目路径root_path
    current_path = os.path.abspath(__file__)  # 文件的绝对路径名 D:\PycharmProjects\api_framework\config\config.py
    root_path = os.path.dirname(os.path.dirname(current_path))

    # 测试数据路径
    data_path = os.path.join(root_path, "data/cases.xlsx")

    # 测试用例路径
    case_path = os.path.join(root_path, "test_cases")

    # config path
    config_path = os.path.join(root_path, "config")

    # 测试报告路径
    report_path = os.path.join(root_path, "report")
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    # # log路径
    # log_path = os.path.join(root_path, "log")

    # yaml 文件路径
    yaml_config_path = os.path.join(config_path, "config.yaml")


class DevConfig(Config):
    # 项目的域名
    host = "http://120.78.128.25:8766/futureloan"


config = DevConfig()
