#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2020/8/28 21:12
# @author：langdawang678
import re


class Context:
    # 上下文/语境，存放临时数据。
    '''
    case依赖/关联，也叫前置条件
    如，充值前要登录成功、
    方式1：setup中登录
    方式2：excel中，把登录case放在最前面
    '''
    member_id = 888
    loan_id = 777
    token = 'aofowelfsf'
    username = 'yuz'

def replace_label(target):
    re_pattern = r'#(.*?)#'
    while re.findall(re_pattern, target):
        # 如果能匹配
        key = re.search(re_pattern, target).group(1)

        target = re.sub(re_pattern, str(getattr(Context, key)), target, 1)
    return target  # 注意return的层级，和while一起


if __name__ == '__main__':
    # print(login())
    # data = save_token()
    # print(data)
    mystr = '{"member_id":"#member_id#","loan_id":"#loan_id#","token":"#token#","username":"#username#"}'
    a = replace_label(mystr)
    print(a)
