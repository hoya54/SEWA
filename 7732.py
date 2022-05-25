from itertools import combinations
import math

t = int(input())


for k in range(t):
    h1, m1, s1 = map(int, input().split(':'))
    h2, m2, s2 = map(int, input().split(':'))
        
    s = s2 - s1
    if s < 0:
        s=(s+60)%60
        m2 -= 1
    if s < 10:
        s = '0' + str(s)

    m = m2 - m1
    if m < 0:
        m=(m+60)%60
        h2 -= 1
    if m < 10:
        m = '0' + str(m)

    h = h2 - h1
    if h < 0:
        h = (h+24)%24
    if h < 10:
        h = '0' + str(h)
    
    print("#{} {}:{}:{}".format(k+1, h, m, s))