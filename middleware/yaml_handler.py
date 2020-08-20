#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2020/8/20 8:53 下午
# @author：langdawang678
import yaml

from config.setting import config


class YamlHandler:
    def __init__(self, file):
        self.file = file

    def read(self, encoding='utf-8'):
        f = open(self.file, encoding=encoding)
        data = yaml.load(f, yaml.FullLoader)
        f.close()
        return data


# 读取本项目的yaml配置
yaml_data = YamlHandler(config.yaml_config_path).read()
print(yaml_data)
