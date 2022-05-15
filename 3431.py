t = int(input())

for k in range(t):
    L, U, X = map(int, input().split())

    if L <= X <= U:
        print("#{}".format(k+1), 0)
    elif U < X:
        print("#{}".format(k+1), -1)
    else:
        print("#{}".format(k+1), L-X)