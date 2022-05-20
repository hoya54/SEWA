
t = int(input())

for k in range(t):
    n, q = map(int, input().split())
    
    lst = [0]*(n+1)

    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            lst[j] = i

    
    
    print("#{}".format(k+1), ' '.join(map(str, lst[1:])))