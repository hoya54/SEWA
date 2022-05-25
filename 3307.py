
t = int(input())


for k in range(t):
    n = int(input())

    lst = list(map(int, input().split()))

    r = [1]*n
    maxx = 1

    for i in range(n):
        for j in range(i):
            if lst[j] <= lst[i]:
                r[i] = max(r[i], r[j]+1)

    print("#{}".format(k+1), max(r))

