from Mat import Mat
from sympy import symbols, simplify, Eq, solve
from fractions import Fraction

F = Fraction

A = Mat([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-7, 0, -1]])
B = Mat([[1, 0, -3, 2], [0, 1, 4, -5], [3, 2, -1, -4]])
C = Mat([[1, -2, -2, -1], [-2, 5, 4, 1], [2, -6, -3, -1], [-2, 3, 5, 3]])
D = Mat([[10, 9, 4, 0], [94, 29, 0, 16], [-84, -20, 4, -16], [64, 2, -12, 16]])

x1, x2, x3, x4 = 1, 2, 3, 4

x = Mat([[x3*F(3, 5)+4*x4], [x3+F(3, 4)*x4], [x3], [x4]])
y = Mat([[x3*F(29, 139)-F(36, 139)*x4],
        [-F(94, 139)*x3+F(40, 139)*x4], [x3], [x4]])
print(D*y)
