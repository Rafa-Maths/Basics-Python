# SECTION 3.3: Loops, branching and functions in Bioinformatics Examples

# List iteration
dna1 = list('ATCGAGCCGACGCAA')
print(dna1)

def count_v1(dna,base):
    i = 0
    for c in dna:
        if c == base:
            i += 1
    return i

a = count_v1(dna1,'A')
print(a)

# String iteration
for c in 'TATCGGGATCATGCATACG':
    print(c)

def count_v2(dna,base):
    i = 0
    for c in dna:
        if c == base:
            i += 1
    return i

dna = 'ATCGTAGCTAGCTA'
base = 'A'
n = count_v2(dna,base)

print('%s appears %d times in %s' %(base,n,dna))

# Index iteration
def count_v3(dna,base):
    i=0
    for j in range(len(dna)):
        if dna[j] == base:
            i += 1
    return i
print(count_v3(dna,base))

# While loops (quite similar as previous)

# Summing a boolean list
def count_v5(dna,base):
    m = []
    for c in dna:
        if c == base:
            m.append(True)
        else:
            m.append(False)
    return sum(m)
print(count_v5(dna,base))

# Inline if test
def count_v6(dna,base):
    m = []
    for c in dna:
        m.append(True if c==base else False)
    return sum(m)
print(count_v6(dna,base))

# Using boolean values directly
def count_v7(dna,base):
    m = []
    for c in dna:
        m.append(c == base)
    return sum(m)
print(count_v7(dna,base))

# List comprehensions
def count_v8(dna,base):
    m = [c==base for c in dna]
    return sum(m)
print(count_v8(dna,base))

def count_v9(dna,base):
    return sum([c==base for c in dna])
print(count_v9(dna,base))

# Using a sum iterator (faster than the previous)
def count_v10(dna,base):
    return sum(c==base for c in dna)
print(count_v10(dna,base))

# Extracting indices
def count_v11(dna,base):
    return len([i for i in range(len(dna)) if dna[i]==base])
print(count_v11(dna,base))


# 3.3.2 EFFICIENCY ASSESSMENT

N = 10000000

# Making a list of random letters and joining all of them to a string
import random
alphabet = list('ATCG')
dna = [random.choice(alphabet) for i in range(N)]
dna = ''.join(dna)
#print(dna)

import time
functions = [count_v1,count_v2,count_v3,count_v5,count_v6,
             count_v7,count_v8,count_v9,count_v10,count_v11]

timings = []
for function in functions:
    t0 = time.perf_counter()
    function(dna,'A')
    t1 = time.perf_counter()
    cpu_time = t1 - t0
    timings.append(cpu_time)
print(timings)

#for cpu_time,function in zip(timings,functions):
#    print('{f:<9s}: {cpu:.2f} s'.format(f=function.func_name,
#                                        cpu=cpu_time))

# Verifying the implementations