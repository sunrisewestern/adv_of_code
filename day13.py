#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-

import json


def as_list(x):
    match x:
        case int() | str():
            return [x]
        case list():
            return x


def check_order(left, right):
    for k in range(max(len(left), len(right))):
        try:
            i = left[k]
        except IndexError:
            return True
        try:
            j = right[k]
        except IndexError:
            return False
        # print(f"i={i},j={j}")
        match i, j:
            case int(), int():
                if i < j:
                    return True
                elif i > j:
                    return False
                else:
                    continue
            case int(), list():
                res = check_order([i], j)
                if isinstance(res, bool):
                    return res
            case list(), int():
                res = check_order(i, [j])
                if isinstance(res, bool):
                    return res
            case list(), list():
                res = check_order(i, j)
                if isinstance(res, bool):
                    return res
            case _:
                raise ValueError("wrong input")


# print(check_order([[1], [2, 3, 4]], [[1], 4]))
# print(check_order([[2, 3, 4]], [[4]]))
# check_order([9], [8])

f = open("./day13_input.txt", "r").read().split("\n\n")
# f = open("./day13_example.txt", "r").read().split("\n\n")

pairs_ls = []
for line in f:
    ls = line.split("\n")
    ls1 = json.loads(ls[0])
    ls2 = json.loads(ls[1])
    pairs_ls.append((ls1, ls2))

is_right_order = []
for idx, pair in enumerate(pairs_ls):
    if check_order(pair[0], pair[1]):
        is_right_order.append(idx + 1)

print(sum(is_right_order))

before_2 = 0
after_6 = 0
for idx, pair in enumerate(pairs_ls):
    for i in pair:
        if check_order(i, [[2]]):
            before_2 += 1
        if check_order([[6]], i):
            after_6 += 1

print(before_2 + 1)
print(len(pairs_ls) * 2 - after_6 + 2)
print((before_2 + 1) * (len(pairs_ls) * 2 - after_6 + 2))
