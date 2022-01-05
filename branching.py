# BRANCHING: if/else tests

from math import *

def f(x):
    if 0 <= x <= pi:
        value = sin(x)
    else:
        value = 0.0
    return value

print(f(pi/2))


C = -30
if C < -273.15:
    print('%g degrees Celsius is non-physical!' %(C))
    print('The Fahrenheit temperature will not be computed')
else:
    F = (9.0/5)*C + 32
    print(F)
print('end of the program')

# Hat function
def N(x):
    if x<0:
        return 0.0
    elif 0<=x<1:
        return x
    elif 1<=x<=2:
        return 2-x
    elif x>=2:
        return 0.0
#def N(x):
#    if 0<=x<1:
#        return x
#    elif 1<=x<2:
#        return 2-x
#    else:
#        return 0.0

print(N(1.3))