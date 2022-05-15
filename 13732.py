t = int(input())

def func(ar, cnt, n):
    for i in range(n):
        for j in range(n):
            if ar[i][j] == 1:
                down = 0
                right = 0
                for k in range(i+1, n):
                    if ar[k][j] == 1:
                        down += 1
                    else:
                        break

                for k in range(j+1, n):
                    if ar[i][k] == 1:
                        right += 1
                    else:
                        break

                if down != right:
                    return 'no'
                for x in range(i, i+down+1):
                    for y in range(j, j+right+1):
                        if ar[x][y] == 1:
                            cnt -= 1
                        else:
                            return 'no'
                if cnt != 0:
                    return 'no'

                return 'yes'

                

for k in range(t):
    n = int(input())

    ar = [[0 for i in range(n)] for i in range(n)]
    cnt = 0
    for i in range(n):
        st = input().rstrip()
        
        for j in range(n):
            c = st[j]

            if c == '#':
                ar[i][j] = 1
                cnt += 1
            else:
                ar[i][j] = 0
    
    r = func(ar, cnt, n)
    print("#{}".format(k+1), r)
    

