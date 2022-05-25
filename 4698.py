from itertools import combinations
import math

t = int(input())

prime = [True]*1000001
p = []

for i in range(2, int(math.sqrt(1000001))+1):
    if prime[i] == True:
        for j in range(i+i, 1000001, i):
            prime[j] = False

for i in range(2, 1000001):
    if prime[i] == True:
        p.append(i)


for k in range(t):
    d, a, b = map(int, input().split())

    lst = []
    for i in p:
        if a <= i <= b:
            lst.append(i)
        
        if i > b:
            break
    
    cnt = 0
    for n in lst:
        if str(d) in list(str(n)):
            cnt += 1
    
    print("#{}".format(k+1), cnt)