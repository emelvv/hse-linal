from Mat import Mat
from sympy import symbols, simplify

a = symbols("\lambda")

A = Mat([[5, 2, -3, 1],
         [a, 1, -4, 3],
         [4, 3, -1, -2]])

A[0] -= A[2]
A.swap_rows(1, 2)
A[1] -= A[0]*4
A[2] = A[2]-A[0]*a
A[1] /= 7
A[0] += A[1]
A[2] -= A[1]*(a+1)
A[2] = A[2]/(a-5)
A[0] += A[2]
A[1] -= A[2]


print(A)
