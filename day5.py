#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-


with open("./day5_input1.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        ls = [line[i : i + 4].strip() for i in range(0, len(line), 4)]

        print(ls)
