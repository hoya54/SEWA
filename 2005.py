t = int(input())

for k in range(t):
    n = int(input())

    ar = []
    for i in range(1, n+1):
        ar.append([0]*i)

    ar[0][0] = 1
    for i in range(1, n):
        for j in range(i+1):
            if j==0 or j==i:
                ar[i][j] = 1
            else:
                ar[i][j] = ar[i-1][j-1] + ar[i-1][j]
    
    print("#{}".format(k+1))
    for i in range(n):
        print(' '.join(map(str, ar[i])))
    
            
