
from collections import deque


t = int(input())

for K in range(t):
    n, k = map(int, input().split())

    total = [0]*(k+1)
    
    team = 1
    for i in range(1, n*k+1):
        line = (i-1)//k

        total[team] += i


        if line%2 == 0:
            if team == k:
                pass
            else:
                team += 1
        else:
            if team == 1:
                pass
            else:
                team -= 1


        
        

    print("#{}".format(K+1), ' '.join(map(str, total[1:])))

