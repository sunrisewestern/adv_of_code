#!/usr/bin/env python3.10
# -*-coding:utf-8 -*-


class Matrix:
    def __init__(self, value=None, nrow=None, ncol=None) -> None:
        if isinstance(value, (tuple, list)):
            self.nrow = len(value)
            self.ncol = len(value[0])
            self._matrix = value
        else:
            self.nrow = nrow
            self.ncol = ncol
            self.shape = (self.nrow, self.ncol)
            self._matrix = [[value for _ in range(nrow) for _ in range(ncol)]]

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
        if isinstance(index, int):
            self._matrix[index] = [_ for _ in value]
        elif isinstance(index, tuple):
            self._matrix[index[0]][index[1]] = value

    def check_visibility(self, i: int, j: int) -> bool:
        if i == 0 or i == self.nrow - 1 or j == 0 or j == self.ncol - 1:
            return True
        else:
            h = self[i, j]
            left = self[i, 0:j]
            right = self[i, j + 1 : self.ncol]
            top = self[0:i, j]
            bottom = self[i + 1 : self.nrow, j]
            if any([_ > h for _ in [*left, *right, *top, *bottom]]):
                return True
            else:
                return False


with open("./day8_input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

mat = Matrix(lines)
mat.ncol
mat.nrow

mat[1, 3]
mat.check_visibility(1, 2)

n_vis = 0
for i in range(mat.nrow):
    for j in range(mat.ncol):
        if mat.check_visibility(i, j):
            n_vis += 1
print(n_vis)
