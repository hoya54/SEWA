import math

t = int(input())

dic ={}
lst = []
for i in range(1, 1000001):
    lst.append(i**3)
    dic[i**3] = i

for k in range(t):
    n = int(input())

    r = -1
    if n in lst:
        r = dic[n]

    
    print("#{}".format(k+1), r)