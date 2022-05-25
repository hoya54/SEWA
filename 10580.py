from itertools import combinations
import math

t = int(input())


for k in range(t):
    n = int(input())

    lst = []
    lst2 = []
    for i in range(n):
        a, b = map(int, input().split())

        

        lst.append((a, b))
        lst2.append((a, b))
    
    cnt = 0

    for i in lst:
        for j in lst2:
            if i == j:
                continue

            if i[0] < j[0]:
                if j[1] < i[1]:
                    cnt += 1
            else:
                if j[1] > i[1]:
                    cnt += 1
    



    print("#{}".format(k+1), cnt//2)