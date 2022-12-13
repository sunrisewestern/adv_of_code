#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-
import re

new_tab = []
with open("./day5_input1.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        ls = [
            line[i : i + 4].strip().replace("[", "").replace("]", "")
            for i in range(0, len(line), 4)
        ]
        new_tab.insert(0, ls)

dic = {
    new_tab[0][i]: [new_tab[j][i] for j in range(1, len(new_tab)) if new_tab[j][i]][
        ::-1
    ]
    for i in range(len(new_tab[0]))
}


def get_new_stacks(n, stack_from, stack_to, dic):
    to_move = dic[stack_from][:n]
    dic[stack_from] = dic[stack_from][n:]
    for i in to_move:
        dic[stack_to].insert(0, i)


with open("./day5_input2.txt", "r") as f:
    for line in f:
        m = re.match(r"move (\d+) from (\d+) to (\d+)", line.strip())
        n, stack_from, stack_to = m.groups()
        print(n, stack_from, stack_to)
        get_new_stacks(int(n), stack_from, stack_to, dic)

print("".join([i[0] for i in dic.values()]))

# %%
dic = {
    new_tab[0][i]: [new_tab[j][i] for j in range(1, len(new_tab)) if new_tab[j][i]][
        ::-1
    ]
    for i in range(len(new_tab[0]))
}


def get_new_stacks(n, stack_from, stack_to, dic):
    to_move = dic[stack_from][:n]
    dic[stack_from] = dic[stack_from][n:]
    dic[stack_to][0:0] = to_move


with open("./day5_input2.txt", "r") as f:
    for line in f:
        m = re.match(r"move (\d+) from (\d+) to (\d+)", line.strip())
        n, stack_from, stack_to = m.groups()
        print(n, stack_from, stack_to)
        get_new_stacks(int(n), stack_from, stack_to, dic)

print("".join([i[0] for i in dic.values()]))

# %%
