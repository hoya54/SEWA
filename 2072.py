n = int(input())

for j in range(n):
    st = list(map(int, input().split()))

    r = 0
    for i in range(10):
        if st[i]%2 == 1:
            r += st[i]
    print("#{}".format(j+1), r)