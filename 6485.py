
t = int(input())

for k in range(t):
    
    n = int(input())

    a = []
    b = []

    station = [0]*5001

    for i in range(n):
        ta, tb = map(int, input().split())
        a.append(ta)
        b.append(tb)

        for j in range(a[i], b[i]+1):
            station[j] += 1
    
    r = []
    p = int(input())
    for i in range(p):
        x = int(input())

        r.append(station[x])


    

        
    
    print("#{}".format(k+1), ' '.join(map(str, r)))
    
