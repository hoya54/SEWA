from itertools import combinations
import math

prime = [True]*1000001

for i in range(2, int(math.sqrt(1000001))+1):
    if prime[i] == True:
        for j in range(i+i, 1000001, i):
            prime[j] = False

r = []
for i in range(2, 1000001):
    if prime[i] == True:
        r.append(i)

print(' '.join(map(str, r)))