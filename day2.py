#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day2.py
@Time    :   2022/12/11 22:01:42
"""


# %% part 1
def cal(x1, x2):
    c1 = {"A": 2, "B": 3, "C": 1}
    c2 = {"X": 2, "Y": 3, "Z": 1}
    res = ["draw", "loss", "win"]  # res[(c1[x1]-c2[x2])%3 ]
    match x2:
        case "X":
            s1 = 1
        case "Y":
            s1 = 2
        case "Z":
            s1 = 3
        case _:
            return None
    match res[(c1[x1] - c2[x2]) % 3]:
        case "win":
            s2 = 6
        case "draw":
            s2 = 3
        case "loss":
            s2 = 0
        case _:
            return None
    s = s1 + s2
    return s


s = 0
with open("./day2_input.txt", "r") as f:
    for line in f:
        ls = line.strip().split(" ")
        score = cal(ls[0].strip(), ls[1].strip())
        print(ls, ls[0], ls[1], score)
        if score:
            s += score
print(s)


# %% part 2
def cal2(x1, r):
    c1 = {"A": 2, "B": 3, "C": 1}
    c2 = {"X": 2, "Y": 3, "Z": 1}
    mod = {"Y": 0, "X": 1, "Z": 2}[r]

    for i in ["X", "Y", "Z"]:
        if (c1[x1] - c2[i]) % 3 == mod:
            x2 = i
            break
    return cal(x1, x2)


s2 = 0
with open("./day2_input.txt", "r") as f:
    for line in f:
        ls = line.strip().split(" ")
        score = cal2(ls[0].strip(), ls[1].strip())
        print(ls, ls[0], ls[1], score)
        if score:
            s2 += score
print(s2)

# %%
