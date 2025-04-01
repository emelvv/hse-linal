from fractions import Fraction
from Mat import Mat
from sympy import sqrt, symbols, solve_univariate_inequality
from copy import deepcopy
print()
print()
F = Fraction
x = symbols('x')
B = Mat([
    [71, 11, 47, 22],
    [11, 28, -19, 58],
    [47, -19, 68, -45],
    [22, 58, -45, 50]
])

old_B = Mat(deepcopy(B[:, :3]))
#############

print(B)

print(B.delta(1))
print(B.delta(2))
print(B.delta(3))
print(B.delta(4))

############
C = Mat(deepcopy(B[:, 3:].T))
B = Mat(deepcopy(B[:, :3]))

# print()

# print(C.T)
# print(old_B)
# print((C.T)*old_B*C)
