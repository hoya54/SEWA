from itertools import combinations
import math

t = int(input())

lst = []
for i in range(1, 10):
    for j in range(1, 10):
        lst.append(i*j)

for k in range(t):
    n = int(input())

    r = ''

    if n in lst:
        r = 'Yes'
    else:
        r = 'No'

    print("#{}".format(k+1), r)