from Mat import Mat
from sympy import symbols

a = symbols("a")
A = Mat([
    [5, -45, 5, 0],
    [-5, 46, -4, 0],
    [-3, 26, -4, 0],
    [-1, 9, a, 0],
    [2, -21, 3, 0]
], slu=3)

A[0] = A[0]/5
A[1] = A[1]+A[0]*5
A[2] = A[2]+3*A[0]
A[3] = A[3]+A[0]
A[4] = A[4]-2*A[0]

A[0] += A[1]*9
A[2] += A[1]
A[4] += A[1]*3

A[4]/=4
A[0]+=-A[4]*10
A[1]+=-A[4]
A[3]+=-(a+1)*A[4]

print(A)
