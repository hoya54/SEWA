
for k in range(10):
    n = int(input())

    lst = []
    for i in range(100):
        st = list(map(int, input().split()))
        lst.append(st)
    
    a, b, c, d = 0, 0, 0, 0

    for i in range(100):
        a = max(a, sum(lst[i]))
    
    for i in range(100):
        s = 0
        for j in range(100):
            s += lst[j][i]
        b = max(b, s)
    
    for i in range(100):
        c += lst[i][i]
    
    for i in range(100):
        d += lst[n-1-i][i]
        

    
    print("#{}".format(k+1), max([a, b, c, d]))




