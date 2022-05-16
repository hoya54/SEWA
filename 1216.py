
for k in range(10):
    T = int(input())
    maxx = 0

    ar = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(100):
        st = input().rstrip()
        for j in range(100):
            ar[i][j] = st[j]

    for i in range(100):
        for j in range(100):
            
            for n in range(1, 101):
                down = []
                right = []
                
                if i+n-1 < 100:
                    for x in range(n):
                        down.append(ar[i+x][j])
                    if down == down[::-1]:
                        maxx = max(maxx, n)
         
                if j+n-1 < 100:
                    for y in range(n):
                        right.append(ar[i][j+y])
                    if right == right[::-1]:
                        maxx = max(maxx, n)

    print("#{}".format(k+1), maxx)