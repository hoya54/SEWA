
t = int(input())


for k in range(t):
    a, b = map(str, input().split())


    ar = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

    for i in range(1, len(b)+1):
        for j in range(1, len(a)+1):
            if a[j-1] == b[i-1]:
                ar[i][j] = ar[i-1][j-1] + 1
            else:
                ar[i][j] = max(ar[i-1][j], ar[i][j-1])
    

    


    
    print("#{}".format(k+1), ar[-1][-1])