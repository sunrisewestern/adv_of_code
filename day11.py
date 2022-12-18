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
    ) -> None:
        self.name = name
        self.items = start_items
        self.operation = operation
        self.divisor = divisor
        self.if_true_monkey_name = None
        self.if_false_monkey_name = None
        self.inspected = 0

    def assign_monkey(self, monkey_dic):
        self.if_true_monkey = monkey_dic[self.if_true_monkey_name]
        self.if_false_monkey = monkey_dic[self.if_false_monkey_name]

    def inspect(self):
        for i in range(len(self.items)):
            self.inspected += 1
            if isinstance(self.items[i], Itemcontainer):
                self.items[i].operate(self.operation)
            else:
                _local = {"old": self.items[i], "new": 0}
                exec(self.operation, _local)
                self.items[i] = math.floor(_local["new"] / 3)

    def throw(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            if isinstance(item, Itemcontainer):
                if item.test(self.divisor):
                    self.if_true_monkey.items.append(item)
                else:
                    self.if_false_monkey.items.append(item)
            else:
                if item % self.divisor == 0:
                    self.if_true_monkey.items.append(item)
                else:
                    self.if_false_monkey.items.append(item)

    def print_items(self):
        items = []
        for item in self.items:
            if isinstance(item, Itemcontainer):
                items.append(item.item_value)
            else:
                items.append(item)
        print(f"{self.name}:\n{items}")


class Itemcontainer:
    def __init__(self, divisors, item_init) -> None:
        self.item_init = item_init
        self.divisors = divisors
        self.item_value = {divisor: item_init % divisor for divisor in divisors}

    def operate(self, operation: str):
        # operation: new = old+6
        for divisor in self.item_value.keys():
            _local = {"old": self.item_value[divisor], "new": None}
            exec(operation, _local)
            self.item_value[divisor] = _local["new"] % divisor

    def test(self, divisor) -> bool:
        if self.item_value[divisor] % divisor == 0:
            return True
        else:
            return False


def initialize(filename):
    monkeys = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Monkey"):
                monkey, _ = line.split(":")
                _, name = monkey.strip().split(" ")
                name = int(name)
                monkeys[int(name)] = Monkey(f"Monkey {name}")
            elif line.startswith("Starting items"):
                _, items = line.split(":")
                items_ls = [int(_.strip()) for _ in items.split(",")]
                monkeys[name].items = items_ls
            elif line.startswith("Operation"):
                _, Operation = line.split(":")
                monkeys[name].operation = Operation.strip()
            elif line.startswith("Test"):
                _, Test = line.split(":")
                _, _, devisor = Test.strip().split(" ")
                monkeys[name].divisor = int(devisor)
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


def run(monkeys, round=1):
    for i in range(round):
        for k in monkeys.keys():
            monkeys[k].inspect()
            monkeys[k].throw()
        if i in (0, 19, 999, 1999):
            print(cal_monkey_business(monkeys))


def run2(monkeys, round=1):
    divisors = [monkey.divisor for monkey in monkeys.values()]
    for k in monkeys.keys():
        monkeys[k].items = [Itemcontainer(divisors, item) for item in monkeys[k].items]
    for i in range(round):
        for k in monkeys.keys():
            monkeys[k].inspect()
            monkeys[k].throw()
        # if i in (0, 19, 999, 1999, ):
        #     print("round", i, " ", cal_monkey_business(monkeys))


# part 1:
# monkeys = initialize("./day11_example.txt")
# run(monkeys, 20)
# print(cal_monkey_business(monkeys))

# part 2
monkeys = initialize("./day11_input.txt")
run2(monkeys, 10000)
print(cal_monkey_business(monkeys))
