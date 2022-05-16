
for k in range(10):
    t = int(input())
    ar = []
    for _ in range(t):
        st = list(map(int, input().split()))
        ar.append(st)
    
    for e in range(100):
        var = 0
        for i in range(100):
            for j in range(100):
                if ar[i][j] == 1:
                    if 0 <= i+1 < 100 and ar[i+1][j] == 0:
                        ar[i+1][j], ar[i][j] = ar[i][j], ar[i+1][j]
                        var += 1
                    elif i+1 == 100:
                        ar[i][j] = 0
                        var += 1
                elif ar[i][j] == 2:
                    if 0 <= i-1 < 100 and ar[i-1][j] == 0:
                        ar[i-1][j], ar[i][j] = ar[i][j], ar[i-1][j]
                        var += 1
                    elif i-1 == -1:
                        ar[i][j] = 0
                        var += 1
        
        if var == 0:
            break
        
    cnt = 0
    for i in range(100):
        for j in range(100):
            if ar[i][j] == 1 and ar[i+1][j] == 2:
                cnt += 1
    
    print("#{}".format(k+1), cnt)