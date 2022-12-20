#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-


class Square:
    __match_args__ = ("x", "y")

    def __init__(self, x: int, y: int, v: str) -> None:
        self.x = x
        self.y = y
        self.v = v
        self.h = {"S": "a", "E": "z"}.get(self.v, self.v)
        self.parent = None
        self.children = None
        self.reverse_c = None

    def __sub__(self, other) -> int:
        return ord(self.h) - ord(other.h)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __repr__(self):
        return f"Square(x={self.x},y={self.y},v={self.v})"


class Map:
    def __init__(self, filename) -> None:
        with open(filename, "r") as f:
            lines = [list(line.strip()) for line in f.readlines()]
        self.nrow = len(lines)
        self.ncol = len(lines[0])
        self.shape = (self.nrow, self.ncol)
        self._matrix = [
            [Square(i, j, v=lines[i][j]) for j in range(self.ncol)]
            for i in range(self.nrow)
        ]

    def __getitem__(self, index):
        # print(index,type(index))
        match index:
            case int():
                return self._matrix[index]
            case slice():
                return self._matrix[index]
            case (int(), int() | slice()):
                return self._matrix[index[0]][index[1]]
            case (slice(), int() | slice()):
                return [_[index[1]] for _ in self._matrix[index[0]]]

    def has(self, i, j):
        if i in range(self.nrow) and j in range(self.ncol):
            return True
        else:
            return False

    def get_passability(self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                self[i, j].children = []
                self[i, j].reverse_c = []
                for i2, j2 in (i, j - 1), (i - 1, j), (i + 1, j), (i, j + 1):
                    if self.has(i2, j2):
                        if self[i2, j2] - self[i, j] <= 1:
                            self[i, j].children.append(self[i2, j2])
                        if self[i, j] - self[i2, j2] <= 1:
                            self[i, j].reverse_c.append(self[i2, j2])

    def inin_start_end(self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                if self[i, j].v == "S":
                    self.start_point = self[i, j]
                if self[i, j].v == "E":
                    self.end_point = self[i, j]

    def BFS(self, start, end):
        search_queue = [start]
        visited_points = []
        while search_queue:
            square = search_queue.pop(0)
            if square not in visited_points:
                visited_points.append(square)
                if square == end:
                    return visited_points.pop()
                else:
                    for n in square.children:
                        if n not in visited_points:
                            n.parent = square
                            search_queue.append(n)
        return None

    def find_shortest_path(self, start, end):
        path = []
        square = end
        n = 1000
        if square:
            while square != start and n > 0:
                n -= 1
                # print(square)
                path.append(square)
                square = square.parent
            return path[::-1]
        else:
            return None

    def clear_parent(self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                self[i, j].parent = None

    def find_a(self, end):
        search_queue = [end]
        visited_points = []
        while search_queue:
            square = search_queue.pop(0)
            if square not in visited_points:
                visited_points.append(square)
                if square.h == "a":
                    return visited_points.pop()
                else:
                    for n in square.reverse_c:
                        if n not in visited_points:
                            n.parent = square
                            search_queue.append(n)


map = Map("./day12_input.txt")

map.get_passability()
map.inin_start_end()
shortest_path = map.find_shortest_path(
    map.start_point, map.BFS(map.start_point, map.end_point)
)
print(len(shortest_path))
map.clear_parent()

shortest_path = map.find_shortest_path(map.end_point, map.find_a(map.end_point))
print(len(shortest_path))
