t = int(input())

for k in range(t):
    a, b = map(int, input().split())

    print("#{}".format(k+1), (a+b)%24)