#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-

s = open("./day6_input.txt", "r").readlines()[0].strip()

for i in range(len(s)):
    block = list(s[i : i + 4])
    print(block)
    if len(set(block)) == 4:
        print(i + 4)
        break

for i in range(len(s)):
    block = list(s[i : i + 14])
    print(block)
    if len(set(block)) == 14:
        print(i + 14)
        break
