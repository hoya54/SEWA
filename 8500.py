t = int(input())

for k in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    
    cnt = n
    if n == 1:
        cnt += 2*lst[0]
    else:
        cnt += lst[0]
        cnt += lst[n-1]
        for i in range(n-1):
            cnt += max(lst[i], lst[i+1])

    print("#{}".format(k+1), cnt)




