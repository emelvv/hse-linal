from fractions import Fraction
from Mat import Mat
from sympy import sqrt, symbols, solve_univariate_inequality
from copy import deepcopy
print()
print()
F = Fraction
a = symbols('a')
B = Mat([
    [1, 1, 0],
    [1, a, -1],
    [0, -1, 2]
])

old_B = Mat(deepcopy(B[:, :3]))
#############

print(B.delta(1))
print(B.delta(2))
print(B.delta(3))

# print(B)

############
C = Mat(deepcopy(B[:, 3:].T))
B = Mat(deepcopy(B[:, :3]))

# print()

# print(C.T)
# print(old_B)
# print((C.T)*old_B*C)
