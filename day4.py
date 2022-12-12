#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day4.py
@Time    :   2022/12/12 00:07:23
"""

# %%
c = 0
with open("./day4_input.txt", "r") as f:
    for line in f:
        ls = line.strip().split(",")
        new_ls = []
        for i in ls:
            i1, i2 = map(int, i.split("-"))
            new = set(range(i1, i2 + 1))
            new_ls.append(new)
        if new_ls[0].issubset(new_ls[1]) or new_ls[1].issubset(new_ls[0]):
            c += 1

print(c)


# %%
c = 0
with open("./day4_input.txt", "r") as f:
    for line in f:
        ls = line.strip().split(",")
        new_ls = []
        for i in ls:
            i1, i2 = map(int, i.split("-"))
            new = set(range(i1, i2 + 1))
            new_ls.append(new)
        if new_ls[0].intersection(new_ls[1]):
            c += 1

print(c)

# %%
