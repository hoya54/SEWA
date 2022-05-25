from itertools import combinations
import math

t = int(input())


for k in range(t):
    s = [0]*13
    d = [0]*13
    h = [0]*13
    c = [0]*13
    

    st = input().rstrip()

    r =''
    for i in range(0, len(st), 3):
        shape = st[i]
        number = int(st[i+1:i+3])

        if shape == 'S':
            if s[number-1] == 1:
                r = "ERROR"
                break
            s[number-1] = 1
        elif shape == 'D':
            if d[number-1] == 1:
                r = "ERROR"
                break
            d[number-1] = 1
        elif shape == 'H':
            if h[number-1] == 1:
                r = "ERROR"
                break
            h[number-1] = 1
        elif shape == 'C':
            if c[number-1] == 1:
                r = "ERROR"
                break
            c[number-1] = 1
    
    if r == 'ERROR':
        print("#{}".format(k+1), r)
    else:
        print("#{}".format(k+1), 13-sum(s), 13-sum(d), 13-sum(h), 13-sum(c))