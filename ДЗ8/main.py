from sympy import I, symbols, sqrt, solve, Eq

z = symbols("z")

expr = 2*sqrt(3)-I

print(solve(Eq(z**4, expr), z))
