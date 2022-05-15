
for k in range(10):
    n = int(input())

    ar = [[0 for _ in range(8)] for _ in range(8)]

    for i in range(8):
        st = input().rstrip()
        for j in range(8):
            ar[i][j] = st[j]
    
    for i in range(8-n+1):
        for j in range(8-n+1):
            
