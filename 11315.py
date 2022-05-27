

t = int(input())


for k in range(t):
    n = int(input())

    ar = [[0 for _ in range(n)] for _ in range(n)]

    
    for i in range(n):
        st = input().rstrip()
        for j in range(n):
            ar[i][j] = st[j]

    flag = False

    for i in range(n):
        for j in range(n):
            if ar[i][j] == 'o':
                if i+4 < n and j+4 < n:

                    p = True
                    for e in range(5):
                        if ar[i+e][j+e] == '.':
                            p = False
                            break
                    if p:
                        flag = True
                if 0 <= i-4 and j+4 < n:
                    p = True
                    for e in range(5):
                        if ar[i-e][j+e] == '.':
                            p = False
                            break
                    if p:
                        flag = True
                if i+4 < n:
                    p = True
                    for e in range(5):
                        if ar[i+e][j] == '.':
                            p = False
                            break
                    if p:
                        flag = True
                if j+4 < n:
                    p = True
                    for e in range(5):
                        if ar[i][j+e] == '.':
                            p = False
                            break
                    if p:
                        flag = True
        if flag:
            break
    
    r =''
    if flag:
        r = 'YES'
    else:
        r = 'NO'
                

    print("#{}".format(k+1), r)
