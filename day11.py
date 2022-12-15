#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-


class Monkey:
    def __init__(self, start_items, operation, test) -> None:
        self.items = start_items
        self.operation = operation
        self.test = test
