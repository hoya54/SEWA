
t = int(input())

for k in range(t):
    n, m = map(int, input().split())

    maxx = 0

    ar = []

    for i in range(n):
        a = list(map(int, input().split()))
        ar.append(a)

        maxx = max(maxx, sum(a))
    
    cnt = 0
    for i in ar:
        if maxx == sum(i):
            cnt += 1

    
    print("#{}".format(k+1), cnt, maxx)