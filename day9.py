#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-


class Knot:
    __match_args__ = ("x", "y")

    def __init__(self, x, y, name=None, pre=None, next=None) -> None:
        self.x = x
        self.y = y
        self.name = name
        self.next = next
        self.pre = pre

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __sub__(self, other):
        if isinstance(other, Knot):
            return Knot(
                self.x - other.x,
                self.y - other.y,
                name=self.name,
                pre=self.pre,
                next=self.next,
            )
        elif isinstance(other, (list, tuple)):
            return Knot(
                self.x - other[0],
                self.y - other[1],
                name=self.name,
                pre=self.pre,
                next=self.next,
            )

    def __add__(self, other):
        if isinstance(other, Knot):
            return Knot(
                self.x + other.x,
                self.y + other.y,
                name=self.name,
                pre=self.pre,
                next=self.next,
            )
        elif isinstance(other, (list, tuple)):
            return Knot(
                self.x + other[0],
                self.y + other[1],
                name=self.name,
                pre=self.pre,
                next=self.next,
            )

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return "Knot(x=%g, y=%g)" % (self.x, self.y)


class Rope:
    def __init__(self, n=2) -> None:
        self.length = n

        if n >= 2:
            self.Head = Knot(0, 0, "head")
            self.Tail = Knot(0, 0, "tail")
            p = self.Head
            for i in range(1, n - 1):
                node = Knot(0, 0)
                p.next = node
                p = p.next
            p.next = self.Tail

            self.tail_trace = [Knot(0, 0)]
        else:
            raise ValueError("No enough knots on rope")

    def print_rope(self):
        p = self.Head
        while p is not None:
            print(p, end="->")
            p = p.next
        print("None")

    def update_knot(self, knot) -> Knot:
        # print(knot - knot.next)
        match knot - knot.next:
            case Knot(x, y) if abs(x) < 2 and abs(y) < 2:
                knot.next = knot.next
            case Knot(0, y) if abs(y) == 2:
                knot.next += 0, int(y / 2)
            case Knot(x, 0) if abs(x) == 2:
                knot.next += int(x / 2), 0
            case Knot(x, y) if abs(x) * abs(y) == 2:
                knot.next += 1 * [1, -1][x < 0], 1 * [1, -1][y < 0]
            case Knot(x, y) if abs(x) == 2 and abs(y) == 2:
                knot.next += 1 * [1, -1][x < 0], 1 * [1, -1][y < 0]
            case _:
                raise ValueError(f"Head moved upexpectively: {knot - knot.next}")

    def update_rope(self):
        p = self.Head
        while p.next is not None:
            self.update_knot(p)
            p = p.next
        self.tail_trace.append(p)

    def move_head_1(self, direction):
        match direction:
            case "L":
                self.Head -= 1, 0
            case "R":
                self.Head += 1, 0
            case "U":
                self.Head += 0, 1
            case "D":
                self.Head -= 0, 1

    def move_head(self, direction, n):
        for i in range(n):
            self.move_head_1(direction)
            self.update_rope()


# part1
rope = Rope(2)
rope.print_rope()

with open("./day9_input.txt", "r") as f:
    for line in f:
        direction, n = line.strip().split(" ")
        rope.move_head(direction, int(n))

print(rope.tail_trace)
print(len(rope.tail_trace))
print(len(set(rope.tail_trace)))

# part2
rope = Rope(10)
rope.print_rope()

with open("./day9_input.txt", "r") as f:
    for line in f:
        direction, n = line.strip().split(" ")
        rope.move_head(direction, int(n))

print(rope.tail_trace)
print(len(rope.tail_trace))
print(len(set(rope.tail_trace)))
