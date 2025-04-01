from fractions import Fraction
from Mat import Mat
from sympy import sqrt
from copy import deepcopy
print()
print()
F = Fraction
B = Mat([[1, 0, 0, 1, 0, 0],
         [0, 6, 0, -F(1, 2), F(1, 2), F(1, 2)],
         [0, 0, -6, F(5, 2), -F(1, 2), F(1, 2)]], slu=3)

old_B = Mat(deepcopy(B[:, :3]))

B[1]/=sqrt(6)
B[:, 1]/=sqrt(6)

B[2]/=sqrt(6)
B[:, 2]/=sqrt(6)

print(B)
C = Mat(deepcopy(B[:, 3:].T))
B = Mat(deepcopy(B[:, :3]))

# print()

# print(C.T)
# print(old_B)
print((C.T)*old_B*C)
