
t = int(input())

for k in range(t):
    n = int(input())

    lst = list(map(int, input().split()))

    avg = sum(lst)/n

    cnt = 0
    
    for i in lst:
        if i <= avg:
            cnt += 1

    print("#{}".format(k+1), cnt)