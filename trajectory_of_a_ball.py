# Computing the trajectory of a ball - Problem Sec 1.8.2

# Defining the variables - SI system
from math import *
g = 9.81
v0 = 15/3.6
theta = pi/3

y0 = 1.0
x = 0.5

y = x*tan(theta) - 1/(2*v0**2)*g*x**2/((cos(theta))**2) + y0

print(y)