# Simple programs to learn how to implement functions

# Section 3.1.1
def F(C):
    return (9.0/5)*C + 32

print(F(5))

def F1(C):
    F_value = (9.0/5)*C + 32
    return ('%5.1f degrees Celsius corresponds to '
            '%5.1f degrees Fahrenheit' % (C, F_value))

print(F1(51.3345))


# Section 3.1.2
def F2(C):
    F = 9./5*C + 32
    return F
dC = 10
C = 30
while C <= 50:
    print('%5.1f %5.1f' % (C, F2(C)))
    C += dC


# Section 3.1.3 - Local and Global Variables
def F3(C):
    F_value = (9.0/5)*C + 32
    print(C, F_value, r)
    return (C, F_value)

C = 60
r = 21
s = F3(r)
print(s)
print(C)

# Example 1 to illustrate how python looks up variables
print(sum)
sum = 500
print(sum)

def myfunc(n):
    sum = n + 1
    print(sum)
    return sum

sum = myfunc(2) + 1
print(sum)

# Example 2 to illustrate how python looks up variables
a = 20
b = -2.5

def f1(x):
    a = 21
    return a*x + b
print(a)
print(f1(1))
print(a)

def f2(x):
    global a
    a = 21
    return a*x + b
print(a)
print(f2(1))
print(a)

# Multiple arguments
g = 9.81
def yfunc(t,v0):
    return v0*t - 0.5*g*t**2

print(yfunc(0.6,6))
print(yfunc(t=0.6,v0=6.0))
print(yfunc(v0=6.0,t=0.6))

# Beyond Mathematical Functions
def makealist(start,stop,inc):
    value = start
    result = []
    while value <= stop:
        result.append(value)
        value += inc
    return result

mylist = makealist(0,5,0.5)
print(mylist)

# Multiple Return Values
g = 9.81
def yfunction(t,v0):
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t
    return y, dydt
position, velocity = yfunction(0.5,3.0)
print(position)
print(velocity)

t_values = [0.1*t for t in range(12)]
for t in t_values:
    position,velocity = yfunction(t,v0=5)
    print( 't=%-10g position=%-10g velocity=%-10g' % (t,position,velocity))

s = yfunction(3.3,5.0)
print(s)
print(type(s))

# Computing Sums
def L(x,n):
    s = 0
#    i = 1
#    while i <= n:
#        s = s + (1.0/i)*(x/(1.0+x))**i
#        i = i + 1
    for i in range(1,n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    return s

print(L(1,10))

def L2(x,n):
    s = 0
    for i in range(1,n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    value_of_sum = s
    first_neglected_term = (1.0/(n+1))*(x/(1.0+x))**(n+1)
    from math import log
    error = log(1+x) - value_of_sum
    return value_of_sum, first_neglected_term, error

sum, firstneglectedterm, error = L2(1,10)
print(sum)
print(firstneglectedterm)
print(error)

# Functions with No Return Values: SUBROUTINES/PROCEDURES
def table(x):
    from math import log
    print('\nx=%g, ln(1+x)=%g' %(x, log(1+x)))
    for n in [1, 2, 10, 100, 500]:
        value, next, error = L2(x,n)
        print('n=%-4d %-10g  (next term: %8.2e error: %8.2e)' \
              %(n,value,next,error))

table(1)

result = table(100)
print(result == None)

# Key word arguments
def somefunc(arg1, arg2, kwarg1=True, kwarg2=0):
    print(arg1, arg2, kwarg1, kwarg2)

somefunc('Hello',[1,2])
somefunc('Hello',[1,2],kwarg1='Hi')
somefunc('Hello',[1,2],kwarg2='Hi')
somefunc('Hello',[1,2],kwarg2='Hi',kwarg1=6)

from math import pi, exp, sin
def f(t, A=1, a=1, omega=2*pi):
    return A*exp(-a*t)*sin(omega*t)
v1 = f(0.2)
print(v1)

def L3(x, epsilon=1.0E-6):
    x = float(x)
    i = 1
    term = (1.0/i)*(x/(1+x))**i
    s = term
    while abs(term) > epsilon:
        i += 1
        term = (1.0/i)*(x/(1+x))**i
        s += term
    return s, i

print(L3(1.71))

# Functions as arguments to Functions
# Example: calculating the second-order derivative of
# a function f numericallly
def diff2nd(f, x, h=1E-5):
    r = (f(x-h)-2*f(x)+f(x+h))/float(h*h)
    return r

def g(t):
    return t**(-6)

t=1.2
d2g = diff2nd(g,t)
print('g"(%f)=%f' %(t,d2g))

for k in range(1,15):
    h = 10**(-k)
    d2g = diff2nd(g,1,h)
    print('h=%.0e: %.5f' %(h,d2g))

# Lambda functions: a compact syntax to define functions
f = lambda x: x**2 + 4
print(f(1))