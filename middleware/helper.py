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
    res = RequestsHandler().visit(config.host + '/member/login',
                                  'post',
                                  json=yaml_data['user'],
                                  headers={"X-Lemonban-Media-Type": "lemonban.v2"}
                                  )
    return res


class Context:
    # 上下文/语境，存放临时数据。
    '''
    case依赖/关联，也叫前置条件
    如，充值前要登录成功、
    方式1：setup中登录
    方式2：excel中，把登录case放在最前面
    '''
    token = ''
    member_id = None


def save_token():
    """保存token信息"""
    # 因为这里的接口入参，需要这样的格式，所以这么拼接
    data = login()

    from jsonpath import jsonpath
    token = jsonpath(data, '$..token')[0]
    token_type = jsonpath(data, '$..token_type')[0]
    member_id = jsonpath(data, '$..id')[0]

    # 拼接json
    token = ' '.join([token_type, token])

    # 用于充值接口前的取数据
    Context.token = token
    Context.member_id = member_id

    return {'token': token, 'memner_id': member_id}


if __name__ == '__main__':
    print(login())
    data = save_token()
    print(data)
