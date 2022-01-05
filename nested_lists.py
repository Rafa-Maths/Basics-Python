# Nested lists

# Simple construction of list of lists / We can think in a matrix here...
Cdgrees = [-5,0,5,10,15]
#Cdgrees = range(-5,20,5) # Compact syntax
Fdgrees = [(9.0/5)*C + 32 for C in Cdgrees]
#print(len(Cdgrees)) # Just for check the construction of the list

table = [Cdgrees, Fdgrees]
print(table)
print(table[0])
print(table[0][2])
print(table[1][4])

# "a transposition of the previous matrix"...
table = []
for C, F in zip(Cdgrees, Fdgrees):
    table.append([C,F])
print(table)

# Pretty print of objects / nicely aligned columns
import pprint
pprint.pprint(table)

for C,F in table:
    print('%5d %5.1f' % (C,F))

# Traversing nested lists in two different ways
scores = []
scores.append([12,16,11,12])
scores.append([9])
scores.append([6,9,11,14,17,15,14,20])

for p in range(len(scores)):
    score_player = [0]*len(scores[p])
    for g in range(len(scores[p])):
        score_player[g] = scores[p][g]
    print(score_player)
    print()

for player in scores:
    print(player)
    print()

# Tuples: "Constant lists"; Advantages: faster codes, protect accidents.
t = (1, 2, 3, 4)
print(t)