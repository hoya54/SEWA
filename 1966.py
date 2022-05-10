t = int(input())

for k in range(t):
    n = int(input())

    lst = list(map(int, input().split()))

    lst.sort()

    print("#{}".format(k+1), ' '.join(map(str, lst)))