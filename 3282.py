
t = int(input())


for K in range(t):
    n, k = map(int, input().split())

    lst = []
    for i in range(n):
        w, v = map(int, input().split())
        lst.append((w, v))
    
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            w = lst[i-1][0]
            v = lst[i-1][1]

            if w <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            else:
                dp[i][j] = dp[i-1][j]
                
    print("#{}".format(K+1), dp[n][k])