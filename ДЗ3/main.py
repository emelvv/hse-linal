import numpy as np
from fractions import Fraction
from sympy import symbols, Eq, solve
import itertools as it

F = Fraction
a = symbols("a")
b = symbols("b")

A = np.array([
    [-9, 6, 7, 10],
    [-6, 4, 2, 3],
    [-3, 2, -11, -15]
])

V = [3, 2, 1]

x = [-(1-2*b-a)/3, b, -11*a, 8*a]
a = []
for i in range(len(A)):
    s = 0
    for j in range(len(A[0])):
        s += A[i, j]*x[j]
    a.append(s == V[i])

print(a)


# A[1] = A[1]-2*A[2]
# A[0] = A[0]-3*A[2]
# A[0] = A[0]/5
# A[1] = A[1]/3

# for i in range(len(A)):
#     for j in range(len(A[0])):
#         print(A[i, j], end=" ")
#     print()


# print(solve(Eq(((4-12/a)/(b-12/a)), 1-a/10), b))
