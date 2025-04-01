from Mat import Mat
from fractions import Fraction

F = Fraction

A = Mat([[2, 0, 0, -4], [1, 2, 0, -3], [0, 1, 0, 0], [-2, 0, 1, 4]])
B = Mat([[F(3, 2), -2, 4, 0], [0, 0, 1, 0], [1, 0, 0, 1], [F(1, 2), -1, 2, 0]])

print(A*B)


