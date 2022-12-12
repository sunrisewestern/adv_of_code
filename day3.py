#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day3.py
@Time    :   2022/12/11 23:23:19
"""
from itertools import islice


def cal(n):
    score = 0
    for i in n:
        if ord("A") <= ord(i) <= ord("Z"):
            score += ord(i) - ord("A") + 27
        else:
            score += ord(i) - ord("a") + 1
    return score


# %% p1
s = 0
with open("./day3_input.txt", "r") as f:
    for line in f:
        ls = list(line.strip())
        size = int(len(ls) / 2)
        ls1 = ls[:size]
        ls2 = ls[size:]
        dup = set(ls1).intersection(set(ls2))
        s += cal(list(dup))

print(s)
# %% p2
f = open("./day3_input2.txt", "r").readlines()

s2 = 0
with open("./day3_input2.txt", "r") as f:
    while True:
        block = list(islice(f, 3))
        if not block:
            break
        ls = list(map(lambda x: set(x.strip()), block))
        dup = set.intersection(*ls)
        s2 += cal(list(dup))


print(s2)

# %%
