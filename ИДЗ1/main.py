from Mat import Mat
from sympy import symbols

A = Mat([[4, -7, -10, 1, -51], [8, -4, 0, 12, -52],
        [6, -5, -4, 7, -49], [-5, 1, -3, -9, 25]], slu=4)


x = symbols("x:1:5")

print(A.check_slu_1(-4-x[3]-2*x[4], 5-2*x[3] - x[4], x[3], x[4]))
