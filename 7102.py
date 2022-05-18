t = int(input())

for k in range(t):
    n, m = map(int, input().split())

    lst = [0]*(n+m+1)

    for i in range(1, n+1):
        for j in range(1, m+1):
            lst[i+j] += 1
    
    maxx = max(lst)

    r = []
    for i in range(1, n+m+1):
        if lst[i] == maxx:
            r.append(i)

    print("#{}".format(k+1), ' '.join(map(str, r)))




