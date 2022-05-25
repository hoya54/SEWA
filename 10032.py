from itertools import combinations
import math

t = int(input())


for k in range(t):
    a, b = map(int, input().split())
    
    if a%b == 0:
        r = 0
    else:
        r = 1
    print("#{}".format(k+1), r)