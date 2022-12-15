#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-


class Register:
    def __init__(self, cycle=1, value=1) -> None:
        self.cycle = cycle
        self.value = value
        self.track = {self.cycle: self.value}

    def addx(self, v):
        self.cycle += 1
        self.track[self.cycle] = self.value
        self.cycle += 1
        self.value += v
        self.track[self.cycle] = self.value

    def noop(self):
        self.cycle += 1
        self.track[self.cycle] = self.value

    def get_signal_stren(self, cycle: int):
        return cycle * self.track[cycle]

    def sprite_pos(self, cycle: int) -> tuple:
        if p := self.track.get(cycle, None):
            pos = p - 1, p, p + 1
            return pos
        else:
            return []


X = Register()

with open("./day10_input.txt", "r") as f:
    for line in f:
        program = line.strip().split(" ")[0]
        if program == "addx":
            value = int(line.strip().split(" ")[-1])
            X.addx(value)
        elif program == "noop":
            X.noop()

# print(X.track)
# print(X.track[180])
# print(X.track[220])

# part 1
sum = 0
for i in range(20, 221, 40):
    score = X.get_signal_stren(i)
    sum += score
    print(i, score)
    print()
print(sum)

max(X.track.values())

# part 2


class Pixel:
    __match_args__ = ("x", "y")

    def __init__(self, x: int, y: int, cycle: int, value=None):
        self.x = x
        self.y = y
        self.cycle = cycle
        self.value = value

    def __repr__(self) -> str:
        return f"Pixel(x={self.x},y={self.y},cycle={self.cycle},value={self.value})"


class Screen:
    def __init__(self, nrow, ncol) -> None:
        self.nrow = nrow
        self.ncol = ncol
        self.shape = (self.nrow, self.ncol)
        self._matrix = [
            [
                Pixel(i, j, j + i * self.ncol + 1, str(j + i * self.ncol + 1))
                for j in range(ncol)
            ]
            for i in range(nrow)
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

    def __setitem__(self, index, value):
        match index:
            case int() if isinstance(value, (tuple, list)):
                for j in range(self.ncol):
                    self._matrix[index][j].value = value[j]
            case slice() if isinstance(value, (tuple, list)):
                for i in index:
                    for j in range(self.ncol):
                        self._matrix[i][j].value = value[j]
            case (int(), int()) if isinstance(value, str):
                self._matrix[index[0]][index[1]].value = value
            case (int(), slice()) | (slice(), int()) | (slice(), slice()) if isinstance(
                value, Screen
            ):
                for i in index[0]:
                    for j in index[1]:
                        self._matrix[i][j].value = value[i, j]

    def draw(self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                pixel = self[i, j]
                cycle = pixel.cycle
                print(pixel.x, pixel.y, pixel.cycle)
                sprite_pos = X.sprite_pos(cycle)
                if pixel.y in sprite_pos:
                    self[i, j] = "#"
                else:
                    self[i, j] = "."

    def write(self, output):
        with open(output, "w") as w:
            for i in range(self.nrow):
                o = [p.value for p in self[i, :]]
                w.write("".join(o) + "\n")


screen = Screen(6, 40)

# screen.write("./day10_output.txt")

# screen.nrow
# screen.ncol
screen.draw()
# print(screen[1, :])

screen.write("./day10_output.txt")
