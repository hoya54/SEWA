t = int(input())


for k in range(t):
    a, b, c = map(int, input().split())

    print("#{}".format(k+1), c//(min(a, b)))
    



