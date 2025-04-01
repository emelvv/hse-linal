from fractions import Fraction
from Mat import Mat
from copy import deepcopy
print()
print()
B = Mat([[1, -2, -3, 1, 0, 0],
         [-2, 6, 5, 0, 1, 0],
         [-3, 5, 12, 0, 0, 1]], slu=3)

old_B = Mat(deepcopy(B[:, :3]))

B[1] += B[0]*2
B[:, 1] += B[:, 0]*2

B[2] += B[0]*3
B[:, 2] += B[:, 0]*3

B[1] /= 2
B[:, 1] /= 2

B[2] += B[1]
B[:, 2] += B[:, 1]

# print(B)
C = Mat(B[:, 3:].T)
B = Mat(deepcopy(B[:, :3]))

print(C.T)
print(old_B)
print(C)
print(C.T*old_B*C)
