from itertools import combinations
import math

t = int(input())


for k in range(t):
    d, l, n = map(int, input().split())


    r = 0
    for i in range(n):
        r += d*(1+i*l/100)
    



    print("#{}".format(k+1), int(r))