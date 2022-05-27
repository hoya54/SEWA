
t = int(input())

for k in range(t):
    n, m = map(int, input().split())
    ar = [[0] * n for _ in range(n)]
    
    dir = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    
    mid = n//2
    ar[mid][mid] = 2
    ar[mid-1][mid-1] = 2
    ar[mid][mid-1] = 1
    ar[mid-1][mid] = 1

    for _ in range(m):
        
        y, x, c = map(int, input().split())
        y -= 1
        x -= 1
        
        
        ar[x][y] = c
        for i in range(8):
            dx, dy = dir[i]
            nx, ny = x + dx, y + dy
            
            reverse = []
            while True:
                if nx < 0 or n - 1 < nx or ny < 0 or n - 1 < ny:
                    reverse = []
                    break
                if ar[nx][ny] == 0:
                    reverse = []
                    break
                if ar[nx][ny] == c:
                    break
                else:
                    reverse.append((nx, ny))
                nx += dx
                ny += dy

            for rx, ry in reverse:
                ar[rx][ry] = c

    w, b = 0, 0
    for i in range(n):
        for j in range(n):
            if ar[i][j] == 1:
                b += 1
            elif ar[i][j] == 2:
                w += 1
                

    print("#{}".format(k+1), b, w)
