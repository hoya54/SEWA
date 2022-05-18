t = int(input())

for k in range(t):
    n, m = map(int, input().split())

    ar = [0]*n
    lst = list(map(int, input().split()))

    for i in lst:
        ar[i-1] = 1
    
    r = []
    for i in range(n):
        if ar[i] == 0:
            r.append(i+1)

    print("#{}".format(k+1), ' '.join(map(str, r)))




