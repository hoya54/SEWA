from itertools import combinations
import math

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

for k in range(t):
    h, w = map(int, input().split())

    ar = [[-1 for _ in range(w+2)] for _ in range(h+2)]

    x, y = 0, 0
    dir = 0

    for i in range(h):
        st = input().rstrip()
        for j in range(len(st)):
            ar[i+1][j+1] = st[j]
            if st[j] in ['<', '>', '^', 'v']:
                x, y = i+1, j+1
                if st[j] == '^':
                    dir = 0
                elif st[j] == '>':
                    dir = 1
                elif st[j] == 'v':
                    dir = 2
                elif st[j] == '<':
                    dir = 3
    
    n = int(input())
    st = list(input().rstrip())

    for c in st:
        if c == 'U':
            dir = 0
            ar[x][y] = '^'
            nx, ny = x+dx[dir], y+dy[dir]
            if ar[nx][ny] == '.':
                ar[nx][ny] = '^'
                ar[x][y] = '.'
                x, y = nx, ny
        elif c == 'D':
            dir = 2
            ar[x][y] = 'v'
            nx, ny = x+dx[dir], y+dy[dir]
            if ar[nx][ny] == '.':
                ar[nx][ny] = 'v'
                ar[x][y] = '.'
                x, y = nx, ny
        elif c == 'L':
            dir = 3
            ar[x][y] = '<'
            nx, ny = x+dx[dir], y+dy[dir]
            if ar[nx][ny] == '.':
                ar[nx][ny] = '<'
                ar[x][y] = '.'
                x, y = nx, ny
        elif c == 'R':
            dir = 1
            ar[x][y] = '>'
            nx, ny = x+dx[dir], y+dy[dir]
            if ar[nx][ny] == '.':
                ar[nx][ny] = '>'
                ar[x][y] = '.'
                x, y = nx, ny
        elif c == 'S':
            px, py = x, y
            px += dx[dir]
            py += dy[dir]

            while True:
                if ar[px][py] == -1:
                    break
                elif ar[px][py] == '#':
                    break
                elif ar[px][py] == '*':
                    ar[px][py] = '.'
                    break
                else:
                    px += dx[dir]
                    py += dy[dir]



    

    print("#{}".format(k+1), ''.join(map(str, ar[1][1:w+1])))
    for i in range(2, h+1):
        print(''.join(map(str, ar[i][1:w+1])))
