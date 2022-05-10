t = int(input())

for k in range(t):
    st = list(map(int, input().split()))

    summ = sum(st)
    summ -= min(st)
    summ -= max(st)

    print("#{}".format(k+1), int(round(summ/8, 0)))