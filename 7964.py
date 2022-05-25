from itertools import combinations
import math

t = int(input())


for k in range(t):
    n, d = map(int, input().split())

    lst = list(map(int, input().split()))

    avail = d
    cur = 0
    cnt = 0

    while True:
        if lst[cur] == 1:
            cur += 1
        else:
            if avail > 1:
                avail -= 1
                cur += 1
            else:
                lst[cur] = 1
                cnt += 1

                avail = d


        if cur == n:
            break



    print("#{}".format(k+1), cnt)