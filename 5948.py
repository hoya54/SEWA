from itertools import combinations
import math

t = int(input())


for k in range(t):
    lst = list(map(int, input().split()))

    r = []
    for i in combinations(lst, 3):
        if sum(i) not in r:
            r.append(sum(i))
    r.sort(reverse=True)

    
    print("#{}".format(k+1), r[4])