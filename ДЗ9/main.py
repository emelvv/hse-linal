from Mat import Mat
from sympy import symbols

a = symbols("a")

A = Mat([[1, 2, 3, 0], 
         [3, 0, 3, 6],
         [-2, -3, -5, -1],
         [1, 4, 5, a]], slu=3)

A[1] = A[1]-3*A[0]
A[2] = A[2]+2*A[0]
A[3] = A[3]-A[0]
A[3] -= A[2]*2
print(A)