
for k in range(10):
    n = int(input())

    x, y = map(int, input().split())

    print("#{}".format(k+1), x**y)