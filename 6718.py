

t = int(input())


for k in range(t):
    
    n = int(input())

    r = 0

    if n < 100:
        r = 0
    elif 100 <= n < 1000:
        r = 1
    elif 1000 <= n < 10000:
        r = 2
    elif 10000 <= n < 100000:
        r = 3
    elif 100000 <= n < 1000000:
        r = 4
    else:
        r = 5

    print("#{}".format(k+1), r)
