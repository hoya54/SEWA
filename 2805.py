t = int(input())

for k in range(t):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)]
    ans = 0  

    m = N//2

    s, e = m, m

    for i in range(N):
        for j in range(s, e+1):
            ans += a[i][j]

        if i < N // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print("#{}".format(k+1), ans)