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
            self._matrix = [[value for _ in range(ncol)] for _ in range(nrow)]

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
            case int():
                self._matrix[index] = [_ for _ in value]
            case slice():
                self._matrix[index] = [_ for _ in value]
            case (int(), int() | slice()):
                self._matrix[index[0]][index[1]] = [_ for _ in value]
            case (slice(), int() | slice()):
                for i in index[0]:
                    for j in index[1]:
                        self._matrix[i][j] = value

    def check_visibility(self, i: int, j: int) -> bool:
        if i == 0 or i == self.nrow - 1 or j == 0 or j == self.ncol - 1:
            return True
        else:
            h = self[i, j]
            left = self[i, 0:j]
            right = self[i, j + 1 : self.ncol]
            top = self[0:i, j]
            bottom = self[i + 1 : self.nrow, j]
            for ls in [left, right, top, bottom]:
                if all([_ < h for _ in ls]):
                    return True
            else:
                return False

    def cal_scenic_score(self, i: int, j: int) -> int:
        h = self[i, j]
        left = self[i, 0:j][::-1]
        right = self[i, j + 1 : self.ncol]
        top = self[0:i, j][::-1]
        bottom = self[i + 1 : self.nrow, j]

        def cal_score(ls, height):
            score = 0
            for n in ls:
                if n < height:
                    score += 1
                else:
                    score += 1
                    break
            return score

        scenic_score = 1
        for ls in [left, right, top, bottom]:
            scenic_score = scenic_score * cal_score(ls, h)
        return scenic_score


with open("./day8_input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

mat = Matrix(lines)
mat.ncol
mat.nrow

mm = Matrix("#", 6, 40)
print(mm._matrix)

mat[1, 3]
print(mat.check_visibility(1, 3))

mat[2, 3]
print(mat.check_visibility(2, 3))


n_vis = 0
for i in range(mat.nrow):
    for j in range(mat.ncol):
        if mat.check_visibility(i, j):
            n_vis += 1
print(n_vis)

scenic_score = 0
for i in range(mat.nrow):
    for j in range(mat.ncol):
        if mat.cal_scenic_score(i, j) > scenic_score:
            scenic_score = mat.cal_scenic_score(i, j)
print(scenic_score)
