t = int(input())

for k in range(t):
    n = int(input())

    ar = [[0 for _ in range(n*3)] for i in range(n)]

    org = []

    for i in range(n):
        st = list(map(int, input().split()))
        org.append(st)
    
    for i in range(n):
        for j in range(n):
            ar[j][n-1-i] = org[i][j]

    for i in range(n):
       for j in range(n):
           ar[j][n-1-i+n] = ar[i][j]

    for i in range(n):
       for j in range(n):
           ar[j][n-1-i+n+n] = ar[i][j+n]
           
    print("#{}".format(k+1))

    for i in range(n):
        print(''.join(map(str, ar[i][:n])), ''.join(map(str, ar[i][n:2*n])), ''.join(map(str, ar[i][2*n:])))



