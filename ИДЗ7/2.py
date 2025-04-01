from fractions import Fraction
from Mat import Mat
from sympy import sqrt, symbols
from copy import deepcopy
print()
print()
F = Fraction
b = symbols('b')
B = Mat([[7, -5, 2],
         [-5, 8*b+10, 4*b-2],
         [2, 4*b-2, 2*b-9]], slu=3)

old_B = Mat(deepcopy(B[:, :3]))
#############

B = B(b, -Fraction(45, 56))
B = B.toList()
B[0].extend([1, 0, 0])
B[1].extend([0, 1, 0])
B[2].extend([0, 0, 1])
B = Mat(B, slu=3)

B[0] /= sqrt(7)
B[:, 0] /= sqrt(7)

B[1] += 5*sqrt(7)/7*B[0]
B[:, 1] += 5*sqrt(7)/7*B[:, 0]

B[2] -= 2*sqrt(7)/7*B[0]
B[:, 2] -= 2*sqrt(7)/7*B[:, 0]

B.swap_cols(1, 2)
B.swap_rows(1, 2)

B[1] /= sqrt(F(313, 28))
B[:, 1] /= sqrt(F(313, 28))

B[2] += -(53*sqrt(2191)/2191)*B[1]
B[:, 2] += -(53*sqrt(2191)/2191)*B[:, 1]

print(B)
############
C = Mat(deepcopy(B[:, 3:].T))
B = Mat(deepcopy(B[:, :3]))

# print()

# print(C.T)
# print(old_B)
# print((C.T)*old_B*C)
