from itertools import combinations
import math

t = int(input())


for k in range(t):
    d, h, m = map(int, input().split())

    d -= 11
    h -= 11
    m -= 11

    
    h += d*24
    m += h*60
    r = m

    if r < 0:
        r = -1


    print("#{}".format(k+1), r)