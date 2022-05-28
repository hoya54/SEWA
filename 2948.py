

from code import interact


t = int(input())


for k in range(t):
    n, m = map(int, input().split())

    a = set(map(str, input().split()))
    b = set(map(str, input().split()))

    c = a.intersection(b)

    print("#{}".format(k+1), len(c))