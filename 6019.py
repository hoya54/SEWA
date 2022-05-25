from itertools import combinations
import math

t = int(input())


for k in range(t):
    d, a, b, f = map(int, input().split())

    time = d/(a+b)

    r = time*f

    print("#{}".format(k+1), r)