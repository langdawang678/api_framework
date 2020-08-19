#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @date: 2020/8/18 22:27
# @author：langdawang678
'''
1.手机号码已经存在
不能手工写在excel
从数据库中找出一条
替换excel中的exist_phone字段


2.注册成功
不能手工写在excel
动态生成
随机生成，判断是否在数据库当中
'''

# coding=utf-8
import random


def gen_mobile():
    """自动生成手机号"""
    phone = '1' + random.choice(['3', '5', '7', '8', '9'])
    for i in range(9):
        num = random.randint(0, 9)
        phone += str(num)
    return phone

if __name__ == '__main__':
    print(gen_mobile())
