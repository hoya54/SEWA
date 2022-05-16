
for k in range(10):
    n = int(input())

    ar = [[0 for _ in range(8)] for _ in range(8)]

    for i in range(8):
        st = input().rstrip()
        for j in range(8):
            ar[i][j] = st[j]

    cnt = 0

    for i in range(8):
        for j in range(8):
            down = []
            right = []
            if i+n-1 < 8:
                for x in range(n):
                    down.append(ar[i+x][j])
                if down == down[::-1]:
                    cnt += 1
            if j+n-1 < 8:
                for y in range(n):
                    right.append(ar[i][j+y])
                if right == right[::-1]:
                    cnt += 1
    print("#{}".format(k+1), cnt)