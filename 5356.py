
t = int(input())

for k in range(t):
    lst = [[-1 for _ in range(15)] for _ in range(5)]

    for i in range(5):
        st = list(input().rstrip())
        for j in range(len(st)):
            lst[i][j] = st[j]
    
    r = ''
    for i in range(15):
        for j in range(5):
            if lst[j][i] != -1:
                r += lst[j][i]
    
        
    
    print("#{}".format(k+1), r)