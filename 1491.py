

t = int(input())


for k in range(t):
    
    n, a, b = map(int, input().split())

    minn = 9999999999

    for r in range(1, n+1):
        for c in range(r, n//r+1):
            if r*c <= n:
                v = a*abs(r-c) + b*(n-r*c)
                minn = min(minn, v)

    
    
    print("#{}".format(k+1), minn)
