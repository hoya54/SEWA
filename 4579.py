from itertools import combinations
import math

t = int(input())


for k in range(t):
    st = input().rstrip()

    n = len(st)

    flag = True

    st = list(st)
    rst = st[:]
    rst.reverse()

    for i in range(n):
        if st[i] ==  rst[i]:
            continue

        if st[i] != rst[i]:
            if st[i] == '*' or rst[i] == '*':
                break
            else:
                flag = False
                break
    

    if flag == True:
        r = 'Exist'
    else:
        r = 'Not exist'
    
    print("#{}".format(k+1), r)