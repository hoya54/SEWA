
t = int(input())

for k in range(t):
    
    n, b, e = map(int, input().split())


    lst = list(map(int, input().split()))

    r = 0

    for x in lst:
        for i in range(b-e, b+e+1):
            if i%x==0:
                r += 1
                break

        
    
    print("#{}".format(k+1), r)
    
