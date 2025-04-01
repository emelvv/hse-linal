from Mat import Mat
from fractions import Fraction
A = Mat([
    [1, 1, 2],
    [8, -7, -4],
    [12, 0, 8],
    [7, 1, 3]
])

A[:, 1] -= A[:, 0] 
A[:, 2] -= 2*A[:, 0]
A[:, 1] /=3
A[:, 2] -= 4*A[:, 1]

print(A)
