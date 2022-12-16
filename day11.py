#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-

import math


class Monkey:
    def __init__(
        self,
        name,
        start_items: list = None,
        operation: str = None,
        divisor: int = None,
        worry_management=None,
    ) -> None:
        self.name = name
        self.items = start_items
        self.operation = operation
        self.divisor = divisor
        self.worry_management = worry_management
        self.if_true_monkey_name = None
        self.if_false_monkey_name = None
        self.inspected = 0

    def assign_monkey(self, monkey_dic):
        self.if_true_monkey = monkey_dic[self.if_true_monkey_name]
        self.if_false_monkey = monkey_dic[self.if_false_monkey_name]

    def inspect(self):
        for i in range(len(self.items)):
            _local = {"old": self.items[i], "new": 0}
            exec(self.operation, _local)
            if self.worry_management:
                exec(self.worry_management, _local)
            self.items[i] = math.floor(_local["new"])
            self.inspected += 1

    def throw(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            if item % self.divisor == 0:
                self.if_true_monkey.items.append(item)
            else:
                self.if_false_monkey.items.append(item)


def initialize(filename):
    monkeys = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Monkey"):
                monkey, _ = line.split(":")
                _, name = monkey.strip().split(" ")
                name = int(name)
                monkeys[int(name)] = Monkey(int(name))
            elif line.startswith("Starting items"):
                _, items = line.split(":")
                items_ls = [int(_.strip()) for _ in items.split(",")]
                monkeys[name].items = items_ls
            elif line.startswith("Operation"):
                _, Operation = line.split(":")
                monkeys[name].operation = Operation.strip()
            elif line.startswith("Test"):
                _, Test = line.split(":")
                _, _, devidend = Test.strip().split(" ")
                monkeys[name].divisor = int(devidend)
            elif line.startswith("If true"):
                _, throw = line.split(":")
                _, _, _, whom = throw.strip().split(" ")
                monkeys[name].if_true_monkey_name = int(whom)
            elif line.startswith("If false"):
                _, throw = line.split(":")
                _, _, _, whom = throw.strip().split(" ")
                monkeys[name].if_false_monkey_name = int(whom)
    for k in monkeys.keys():
        monkeys[k].assign_monkey(monkeys)
    return monkeys


def cal_monkey_business(monkeys) -> list:
    res = []
    for k in monkeys.keys():
        res.append(monkeys[k].inspected)
    print(res)
    monkey_business = sorted(res, reverse=True)[0] * sorted(res, reverse=True)[1]
    return monkey_business


def worry_manage(monkeys, new_management):
    for k in monkeys.keys():
        monkeys[k].worry_management = new_management


def run(monkeys, round=1):
    for i in range(round):
        for k in monkeys.keys():
            monkeys[k].inspect()
            monkeys[k].throw()
        if i in (0, 19, 999, 1999):
            print(cal_monkey_business(monkeys))


# monkeys = initialize("./day11_example.txt")
# worry_manage(monkeys, "new = new/3")
# run(monkeys, 20)
# print(cal_monkey_business(monkeys))


monkeys = initialize("./day11_example.txt")
run(monkeys, 20)
print(cal_monkey_business(monkeys))
