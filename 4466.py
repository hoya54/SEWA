t = int(input())

for k in range(t):
    n, w = map(int, input().split())

    lst = list(map(int, input().split()))

    lst.sort(reverse=True)

    r = sum(lst[:w])

    print("#{}".format(k+1), r)




