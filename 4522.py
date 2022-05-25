from itertools import combinations
import math

t = int(input())


for k in range(t):
    st = input().rstrip()

    n = len(st)

    flag = True
    for i in range(n//2):
        if st[i] == '?' or st[n-1-i] == '?':
            continue

        if st[i] != st[n-1-i]:
            flag = False
            break
    
    # if '?' not in list(st):
    #    flag = False

    if flag == True:
        r = 'Exist'
    else:
        r = 'Not exist'
    
    print("#{}".format(k+1), r)