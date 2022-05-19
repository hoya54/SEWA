t = int(input())

for k in range(t):
    n, m = map(int, input().split())

    y = n - m
    x = m - y

    print("#{}".format(k+1), x, y)




