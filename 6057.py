
t = int(input())


for k in range(t):
    n, m = map(int, input().split())

    lst = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())

        lst[x][y] = 1
        lst[y][x] = 1

    
    cnt = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for e in range(j+1, n+1):
                if lst[i][j] == 1 and lst[j][e] == 1 and lst[e][i] == 1:
                    cnt += 1
    

    


    
    print("#{}".format(k+1), cnt)