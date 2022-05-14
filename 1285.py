t = int(input())

for k in range(t):
    n = int(input())

    st = list(map(int, input().split()))

    lst = []
    for i in range(n):
        lst.append(abs(st[i]))
    minn = min(lst)
    c = lst.count(minn)

    print("#{}".format(k+1), minn, c)
