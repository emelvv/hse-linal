import numpy as np
from fractions import Fraction
import sympy
import copy


class Mat():
    __slots__ = ["_arr", "_slu"]

    def __init__(self, arr, slu: int = -1):
        self._slu = slu
        if len(np.array(arr).shape) != 2:
            raise Exception("Not matrix.")

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if isinstance(arr[i][j], sympy.core.Basic):
                    continue
                arr[i][j] = Fraction(arr[i][j])

        self._arr = np.array(arr)

    def __str__(self):
        s = ""
        for i, x in enumerate(self._arr):
            for j, y in enumerate(x):
                if j == self._slu:
                    s += "| "
                s += str(y)+" "
            s += "\n"
        return s

    def __mul__(self, other):
        if isinstance(other, Mat):
            return Mat(np.dot(self._arr, other._arr))
        return Mat(self._arr * other)

    def __rmul__(self, other):
        if isinstance(other, Mat):
            return Mat(np.dot(other._arr, self._arr))
        return Mat(self._arr * other)

    def __add__(self, other):
        if isinstance(other, Mat):
            return Mat(self._arr + other._arr)
        return Mat(self._arr + other)

    def __radd__(self, other):
        if isinstance(other, Mat):
            return Mat(self._arr + other._arr)
        return Mat(self._arr + other)

    def __sub__(self, other):
        if isinstance(other, Mat):
            return Mat(self._arr - other._arr)
        return Mat(self._arr - other)

    def __rsub__(self, other):
        if isinstance(other, Mat):
            return Mat(other._arr-self._arr)
        return Mat(other - self._arr)

    def __pos__(self):
        return Mat(self._arr)

    def __neg__(self):
        return Mat(-self._arr)

    def __pow__(self, n):
        return Mat(np.linalg.matrix_power(self._arr, n))

    def __getitem__(self, index):
        return self._arr[index]

    def __setitem__(self, index, value):
        self._arr[index] = value

    def swap(self, ind1, ind2):
        row1 = copy.copy(self._arr[ind1])
        self._arr[ind1] = self._arr[ind2]
        self._arr[ind2] = row1

    def check_slu_1(self, *xs):
        if self._slu == -1:
            raise Exception("Not SLU.")
        if len(self._arr[0]) - self._slu != 1:
            raise Exception("Not SLU-1")
        if len(xs) != len(self._arr[0])-1:
            raise Exception("The number of x's does not match.")

        for row in self._arr:
            s = 0
            for i in range(len(xs)):
                s += xs[i]*row[i]
            if s != row[-1]:
                return False
        return True

    @property
    def T(self):
        return Mat(self._arr.T)

    @property
    def tr(self):
        return np.trace(self._arr)
