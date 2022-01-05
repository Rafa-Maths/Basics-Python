# How to work with complex numbers
from math import *
#from cmath import *
r = 1
theta = pi/4
u = r*(sin(theta) + cos(theta)*1j)
v = complex(r*sin(theta),r*cos(theta))

real_part = u.real
imag_part = u.imag
conjugate = u.conjugate()

print(u)
print(v)
print(real_part)
print(imag_part)
print(conjugate)
#print("""u is: %
#v is: %""" %(u,v))