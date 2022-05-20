
t = int(input())

for k in range(t):
    n = int(input())

    st = list(map(int, input().split()))

    cnt = 0
    for i in range(1, n-1):
        if st[i] != max([st[i-1], st[i], st[i+1]]) and st[i] != min([st[i-1], st[i], st[i+1]]):
            cnt += 1
    

    print("#{}".format(k+1), cnt)
    