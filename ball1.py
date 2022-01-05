# Program for computing the height of a ball in vertical motion
v0 = 5.0
g = 9.81
t = 0.6

y = v0*t - 0.5*g*t**2

print("""At t=%.3f s, a ball with
initial velocity v0=%.3f m/s
is located at height of %.5f m""" %(t,v0,y))

# Differences between float division and integer division
C = 21
F = (9/5)*C + 32
print(F)
F = (9//5)*C + 32
print(F)