#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2020/8/20 8:45 下午
# @author：langdawang678

from common.requests_handler import RequestsHandler
from config.setting import config
from middleware.yaml_handler import yaml_data


def login():
    """
    # 数据方案1：从login的excel中获取
    # 数据方案2：从配置文件中获取
    """
    res = RequestsHandler().visit(config.host+'/member/login',
                                  'post',
                                  json=yaml_data['user'],
                                  headers={"X-Lemonban-Media-Type": "lemonban.v2"}
                                  )
    return res

def save_token():
    pass

if __name__ == '__main__':
    print(login())

