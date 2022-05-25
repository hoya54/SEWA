from itertools import combinations
import math

t = int(input())


for k in range(t):
    st = input().rstrip()

    lst = []

    i=0
    while i < len(st):
        if st[i] == 'n':
            lst.append('N')
            i += 5
        else:
            lst.append('W')
            i += 4

    lst.reverse()

    dir = 0

    if lst[0] == 'N':
        dir = 0
    else:
        dir = 90

    del lst[0]

    j = 1
    for i in lst:
        if i == 'N':
            dir = dir - (90/2**j)
        else:
            dir = dir + (90/2**j)
        
        j += 1
    j=1

    while True:
        if dir != int(dir):
            dir *= 2
            j *= 2
        else:
            break

    print("#{} {}/{}".format(k+1, int(dir), j))