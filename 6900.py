from itertools import combinations
import math

t = int(input())


for k in range(t):
    n, m = map(int, input().split())

    lst = []
    for i in range(n):
        gou, value = map(str, input().split())
        value = int(value)
        lst.append((gou, value))
    
    my = []
    for i in range(m):
        myno = input().rstrip()
        my.append(myno)

    r = 0

    for i in range(m):
        
        for j in range(n):
            flag = True
            for d in range(8):
                if lst[j][0][d] == '*':
                    continue
                else:
                    if my[i][d] != lst[j][0][d]:
                        flag = False
                        break
            if flag == True:
                r += lst[j][1]
                break



    print("#{}".format(k+1), r)