from itertools import combinations
import math

t = int(input())


for k in range(t):
    lst = list(map(str, input().split()))

    bp = 1
    op = 1

    bw = 0
    ow = 0

    time = 0
    for i in range(1, len(lst), 2):
        who, number = lst[i], int(lst[i+1])

        if who == 'B':
            
            need = max(0, abs(number-bp) - bw) +1
            bp = number
            bw = 0

            time += need
            ow += need
        else:
            need = max(0, abs(number-op) - ow) +1
            op = number
            ow = 0
            
            time += need
            bw += need


    print("#{}".format(k+1), time)