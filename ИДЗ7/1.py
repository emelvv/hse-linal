from fractions import Fraction
from Mat import Mat
from sympy import sqrt
from copy import deepcopy
print()
print()
F = Fraction
B = Mat([[-81, 54, 63, 1, 0, 0],
         [54, -40, -46, 0, 1, 0],
         [63, -46, -102, 0, 0, 1]], slu=3)

old_B = Mat(deepcopy(B[:, :3]))

B[0] /= sqrt(81)
B[:, 0] /= sqrt(81)

B[1] += 6*B[0]
B[:, 1] += 6*B[:, 0]

B[2] += 7*B[0]
B[:, 2] += 7*B[:, 0]

B[2] -= B[1]
B[:, 2] -= B[:, 1]

B[1] /= 2
B[:, 1] /= 2

B[2] /= 7
B[:, 2] /= 7


print(B)
C = Mat(deepcopy(B[:, 3:].T))
B = Mat(deepcopy(B[:, :3]))

# print()

# print(C.T)
# print(old_B)
# print((C.T)*old_B*C)
