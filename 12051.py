
t = int(input())

        

for k in range(t):
    n, d, g = map(int, input().split())

    r = ''
    if d != 0 and g == 0:
        r = 'Broken'
    elif d != 100 and g == 100:
        r = 'Broken'
    else:
        check = 0
        for q in range(1,n+1):
            
            if q*d/100 == q*d//100:
                check = 1
                break
        if check == 1:
            r = 'Possible'
        else:
            r = 'Broken'


    print("#{}".format(k+1), r)
    
    
        
