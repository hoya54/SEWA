

t = int(input())


r = []
for k in range(t):
    n, x = map(int, input().split())

    

    lst = list(map(int, str(x)))

    lst.reverse()

    N = 0
    for i in range(len(lst)):
        N += (lst[i]*(n**i))%(n-1)
    
    print("#{}".format(k+1), N%(n-1))