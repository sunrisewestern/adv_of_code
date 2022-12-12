#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day_1.py
@Time    :   2022/12/11 21:38:27
"""

f = open("./day1_input.txt", "r").read().split("\n\n")

ls = [map(lambda x: int(x.strip()), l.split("\n")) for l in f]

ls_sum = [sum(l) for l in ls]
max(ls_sum)

sum(sorted(ls_sum, reverse=True)[0:3])
