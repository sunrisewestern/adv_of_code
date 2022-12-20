#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-


# sand (500,0)
# air
# rock


class Point:
    __match_args__ = ("x", "y")

    def __init__(self, x: int, y: int, v: str = None) -> None:
        self.x = x
        self.y = y
        self.v = v

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point(x={self.x},y={self.y},v={self.v})"


class Map:
    def __init__(self, min_x, max_x, min_y, max_y) -> None:
        self.min_x = min_x
        self.min_y = min_y
        self.x_range = range(min_x, max_x + 1)
        self.y_range = range(min_y, max_y + 1)
        self._matrix = [
            [Point(x, y, "air") for y in range(min_y, max_y + 1)]
            for x in range(min_x, max_x + 1)
        ]

    def __repr__(self):
        return f"Map(min_x={self.min_x}, max_x={self.max_x}, min_y={self.min_y}, max_y={self.max_y})"

    def __getitem__(self, index):
        match index:
            case int():
                return self._matrix[index - self.min_x]
            case slice():
                return self._matrix[index.start - self.min_x : index.stop - self.min_x]
            case (int() | slice(), int() | slice()):
                if isinstance(index[1], int):
                    y = index[1]
                elif isinstance(index[1], slice):
                    y = slice(index[1].start - self.min_y, index[1].stop - self.min_y)

                if isinstance(index[0], int):
                    return self._matrix[index[0] - self.min_x][y]
                elif isinstance(index[0], slice):
                    return [
                        _[y]
                        for _ in self._matrix[
                            index[0].start - self.min_x : index[0].stop - self.min_x
                        ]
                    ]
            case _:
                raise IndexError()

    def set_rocks(self, paths):
        for path in paths:
            for i, j in path:
                self[i, j].v = "rock"


def make_path(path_points: list):
    whole_path = [_ for _ in path_points]
    for p1, p2 in zip(path_points, path_points[1:]):
        match [p1, p2]:
            case [(x1, y1), (x2, y2)]:
                if x1 == x2:
                    whole_path += [
                        (x1, _) for _ in range(y1, y2, int((y2 - y1) / abs(y2 - y1)))
                    ]
                elif y1 == y2:
                    whole_path += [
                        (_, y1) for _ in range(x1, x2, int((x2 - x1) / abs(x2 - x1)))
                    ]
                else:
                    raise ValueError("Wrong Path Point")
            case _:
                raise TypeError("Wrong input type")
    # print(whole_path)
    whole_path = sorted(list(set(whole_path)))
    return whole_path


input = "./day14_example.txt"
path_points = []
with open(input, "r") as f:
    for line in f:
        ls = [tuple(_.strip().split(",")) for _ in line.strip().split("->")]
        ls2 = [(int(i[0]), int(i[1])) for i in ls]
        new_ls = make_path(ls2)
        path_points.append(new_ls)


all_points = [point for path in path_points for point in path] + [(500, 0)]
max_x = max([_[0] for _ in all_points])
min_x = min([_[0] for _ in all_points])
max_y = max([_[1] for _ in all_points])
min_y = min([_[1] for _ in all_points])

map = Map(min_x, max_x, min_y, max_y)
map._matrix
map.set_rocks(path_points)
