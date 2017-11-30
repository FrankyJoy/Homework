#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MyObject.py
# @Author: He Peng
# @Date  : 2017/11/30
# @Desc  : 数据对象

# 对象表列名：id c_value c_time c_fren
class SingleData:
    def __init__(self,id,c_value,c_time,c_fren):
        self.id = id
        self.value = c_value
        self.time = c_time
        self.fren = c_fren
        pass
