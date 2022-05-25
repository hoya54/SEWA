from itertools import combinations
import math

t = int(input())


for k in range(t):
    a, b = map(int, input().split())

    n = a//b

    cnt = 0
    j = 1
    for i in range(n):
        cnt += j
        j += 2
    

    print("#{}".format(k+1), cnt)