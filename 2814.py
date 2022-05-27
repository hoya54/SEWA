

t = int(input())

def dfs(i,cnt):
    global maxx
    global visit

    
    maxx = max(maxx, cnt)

    for e in range(1, n+1):
        if g[i][e] and not visit[e]:
            visit[e] = 1
            dfs(e,cnt+1)
            visit[e] = 0

for k in range(t):
    n, m = map(int, input().split())

    g = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())
        g[x][y] = 1
        g[y][x] = 1

    maxx = 1

    for i in range(1, n+1):
        visit = [0]*(n+1)
        visit[i] = 1
        dfs(i, 1)




    print("#{}".format(k+1), maxx)