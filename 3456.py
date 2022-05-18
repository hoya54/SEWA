t = int(input())

for k in range(t):
    
    lst = list(map(int, input().split()))
    lst.sort()

    print("#{}".format(k+1), lst[0]+lst[2]-lst[1])




