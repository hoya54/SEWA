from itertools import permutations
import math

t = int(input())

o = [i for i in range(1, 19)]

for k in range(t):
    lst = list(map(int, input().split()))

    cnt = 0

    enemy = []
    for i in range(1, 19):
        if i not in lst:
            enemy.append(i)
    
    for case in permutations(enemy, 9):
        ls, es = 0, 0

        for i in range(9):
            l, r = lst[i], case[i]

            if l > r:
                ls += (lst[i]+case[i])
            else:
                es += (lst[i]+case[i])
        
        if ls > es:
            cnt += 1

    
    print("#{}".format(k+1), cnt, math.factorial(9)-cnt)

    

        
        


