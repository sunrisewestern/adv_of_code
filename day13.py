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
        match i, j:
            case int(), int():
                if i <= j:
                    return True
                else:
                    return False
            case int(), list():
                check_order([i], j)
            case list(), int():
                check_order(i, [j])
            case list(), list():
                check_order(i, j)
            case _:
                raise ValueError("wrong input")


# f = open("./day13_input.txt", "r").read().split("\n\n")
f = open("./day13_example.txt", "r").read().split("\n\n")

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
    else:
        print(pair[0])
        print(pair[1])
        print()

print(sum(is_right_order))
