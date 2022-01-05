# Basic symbolic computing -
# differentiation, integration, equation solving, taylor series,...
from sympy import (symbols,Rational,diff,integrate,lambdify)

t, v0, g = symbols('t v0 g')
y = v0*t - Rational(1, 2)*g*t ** 2

dydt = diff(y, t)
print('velocity:', dydt)

dy2dt2 = diff(y,t,t)
print('aceleration:', dy2dt2)

y2 = integrate(dydt,t)
print(y2)

y3 = integrate(dy2dt2, t)
print(y3)

v = lambdify([t,v0,g],dydt)
print(v(2,5,9.81))

from sympy import solve

roots = solve(y,t)
print(roots)
print(y.subs(t,roots[0]))
print(y.subs(t,roots[1]))

from sympy import exp, sin, cos, latex, simplify, expand

f = exp(t)
print(f.series(t,0,5))

f = exp(sin(t))
print(latex(f.series(t,0,8)))

x,y = symbols('x,y')
f = -sin(x)*sin(y) + cos(x)*cos(y)
print(simplify(f))
print(expand(sin(x+y), trig=True))