from Mat import Mat
from sympy import symbols

x = symbols("x")

A = Mat([[1, 3, x, -2, x], [x, 2, 0, 4, 5], [0, -1, x, 1, -3],
        [3, x, -1, 2, -3], [-1, -2, 4, x, -2]])


print(A.det)