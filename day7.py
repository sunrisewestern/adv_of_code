#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-


class TreeNode:
    def __init__(self, name, is_dir: bool, size=None) -> None:
        self.name = name
        self.size = size
        self.is_dir = is_dir
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_size(self):
        if self.is_dir:
            total = 0
            for child in self.children:
                size = child.get_size()
                total += size
            return total
        else:
            return self.size


Tree = {}

with open("./day7_input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "$ cd /":
            Tree["root"] = TreeNode(name="root", is_dir=True)
            current = Tree["root"]
        elif line == "$ ls":
            continue
        elif "$" not in line:
            size, name = line.split(" ")
            if size != "dir":
                Tree[f"{current.name}/{name}"] = TreeNode(
                    name=name,
                    size=int(size),
                    is_dir=False,
                )
            else:
                Tree[f"{current.name}/{name}"] = TreeNode(name=name, is_dir=True)
            current.add_child(Tree[f"{current.name}/{name}"])
            continue
        elif line == "$ cd ..":
            current = current.parent
        elif "$ cd" in line:
            name = line.split(" ")[2]
            current = Tree[f"{current.name}/{name}"]

part1 = 0
for name, node in Tree.items():
    if node.is_dir:
        node.size = node.get_size()
        print(name, node.size)
        if node.size <= 100000:
            part1 += node.size


print("\ntotal:", part1)
