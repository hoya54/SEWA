n = int(input())

for j in range(n):
    st = list(map(int, input().split()))

    r = max(st)
    print("#{}".format(j+1), r)