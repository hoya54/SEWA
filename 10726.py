from itertools import combinations
import math

t = int(input())


for k in range(t):
    n, m = map(int, input().split())

    m = bin(m)

    m = m[-n:]


    if m == '1'*len(m):
        r = 'ON'
    else:
        r = 'OFF'

    print("#{}".format(k+1), r)