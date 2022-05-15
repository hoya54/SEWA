t = int(input())

for k in range(t):
    a, b = map(int, input().split())

    if a > 9 or b > 9:
        print("#{}".format(k+1), -1)
    else:
        print("#{}".format(k+1), a*b)