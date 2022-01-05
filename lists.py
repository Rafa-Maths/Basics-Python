# Simple program to implement lists

# Basic operations with lists
C = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
C.append([45, 50, 55])
C.append(60)

C.insert(0,-25)
C.insert(2, -17.5)

C = C + [65, 70]
C = [-30] + C

del C[10]

print(len(C))
print(C)
print(C.index(20))
print(20 in C)
print(21 in C)
print(C[0])
print(C[-3])

# Creating a list with the comand while
L = []
L_value = -2
L_max = 2
while L_value <= L_max:
    L.append(L_value)
    L_value = L_value + 0.5
print(L)

# Creating variables to refer to various lists
somelist = ['book.tex', 'book.log', 'book.pdf']
texfile, logfile, pdf = somelist
print(texfile)
print(logfile)
print(pdf)

# Comand for
degrees = [0,10,20,40,100]
for T in degrees:
    print('list element', T)
print('The degrees list has', len(degrees), 'elements')

# Printing the table in a nice format
print('    C    F')
for T in degrees:
    F = (9.0/5)*T + 32
    print('%5d %5.1f' % (T, F))

# Comand range
Cdegrees = range(-3, 2, 2)
print(Cdegrees[2])

# Compact syntax for list comprehension
Cdegrees = [-5 + i*1.5 for i in range(10)]
print(Cdegrees)
Fdegrees = [(9.0/5)*T + 32 for T in Cdegrees]
print(Fdegrees)
C_plus_5 = [T+5 for T in Cdegrees]
print(C_plus_5)

# Traversing multiple lists simultaneously
for T0, T1, T2 in zip(Cdegrees, Fdegrees, C_plus_5):
    print('%3f %5.1f %3f' % (T0, T1, T2))