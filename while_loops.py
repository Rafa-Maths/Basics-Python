# Simple program to implement while loops

print("----------")
C = -20.0
dC = 5
while C<=40:
    F = (9.0/5)*C + 32
    print(C, F)
    C = C + dC
print("----------")

from math import *
x = pi/4

sum = 0.0
N = 30
k = 1
sign = -1
while k<=N:
    sign = -1*sign
    sum = sum + sign*(x**(2*k-1))/factorial(2*k-1)
    k = k+1
print('sin(%g) = %g (approximation with %g terms)' % (x, sum, N))