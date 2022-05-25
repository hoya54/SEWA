
from collections import deque


t = int(input())

for k in range(t):
    n, m = map(int, input().split())

    wait = deque()

    space = [0]*(n+1)
    space[0] = 1

    cost = [0]*(n+1)
    weight = [0]*(m+1)

    for i in range(n):
        v = int(input())
        cost[i+1] = v
    
    for i in range(m):
        w = int(input())
        weight[i+1] = w

    total = 0
    for _ in range(2*m):
        i = int(input())
        if i > 0:
            full = 1
            for j in range(1, n+1):
                if space[j] == 0:
                    space[j] = i
                    total += cost[j]*weight[i]
                    full = 0
                    break
            if full:
                wait.append(i)
            
        else:
            i *= -1
            for j in range(1, n+1):
                if space[j] == i:
                    space[j] = 0
                    break
            
            if wait:
                i = wait.popleft()
                for j in range(1, n+1):
                    if space[j] == 0:
                        space[j] = i
                        total += cost[j]*weight[i]
                        break


        
    print("#{}".format(k+1), total)

