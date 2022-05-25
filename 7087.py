from itertools import combinations
import math

t = int(input())


for k in range(t):
    n = int(input())

    ar = [0]*26

    for i in range(n):
        st = input().rstrip()
        c = st[0]

        ar[ord(c)-65] += 1
    
    cnt = 0
    for i in range(26):
        if ar[i] != 0:
            cnt += 1
        else:
            break
            






    print("#{}".format(k+1), cnt)