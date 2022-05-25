from itertools import combinations
import math

t = int(input())


for k in range(t):
    n, m = map(int, input().split())

    lst = list(map(int, input().split()))

    lst.sort(reverse=True)

    maxx = -1

    for i in range(n-1):
        if lst[i] > m:
            continue
        
        for j in range(i+1, n):
            if lst[i]+lst[j] <= m:
                maxx = max(maxx, lst[i]+lst[j])

    

    print("#{}".format(k+1), maxx)