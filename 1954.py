t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



for k in range(t):
    n = int(input())

    ar = [[0 for _ in range(n)] for _ in range(n)]
    c = 1
    ar[0][0] = c
    c += 1
    dir = 0
    x=0
    y=0

    for i in range(n):
        for j in range(n):
            if i==0 and j==0:
                continue
                
            x += dx[dir]
            y += dy[dir]

            if  0 <= x < n and 0 <= y < n and ar[x][y] == 0:
                ar[x][y] = c
                c += 1
            else:
                x -= dx[dir]
                y -= dy[dir]

                dir = (dir+1)%4
                x += dx[dir]
                y += dy[dir]

                ar[x][y] = c
                c += 1


    print("#{}".format(k+1))
    for i in range(n):
        print(' '.join(map(str, ar[i])))
    


