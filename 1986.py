t = int(input())

for k in range(t):
    s = 0
    n = int(input())
    for i in range(1, n+1):
        if i%2 == 1:
            s += i
        else:
            s -= i
    print("#{}".format(k+1), s)