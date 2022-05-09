
t = int(input())

for k in range(t):
    n, m = map(int, input().split())
    ar = []

    for i in range(n):
        st = list(map(int, input().split()))
        ar.append(st)
    
    maxx = 0
    
    for x in range(n-m+1):
        for y in range(n-m+1):
            summ = 0
            for i in range(x, x+m):
                for j in range(y, y+m):
                    summ += ar[i][j]
            
            maxx = max(maxx, summ)
    print("#{}".format(k+1), maxx)

