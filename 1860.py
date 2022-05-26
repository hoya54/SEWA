

t = int(input())


for k in range(t):
    
    n, m, K = map(int, input().split())

    lst = list(map(int, input().split()))

    lst.sort(reverse=True)


    
    stock = 0

    flag = True

    for time in range(10000):
        if time > 0 and time % m == 0:
            stock += K
        if lst and lst[-1] == time:
            lst.pop()
            if stock == 0:
                flag = False
                break
            else:
                stock -= 1
    
    if flag:
        r = 'Possible'
    else:
        r = 'Impossible'
    
    print("#{}".format(k+1), r)
