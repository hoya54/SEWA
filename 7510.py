
t = int(input())

for k in range(t):
    n = int(input())

    cnt = 0
    for i in range(1, n+1):
        s=0
        for j in range(i, n+1):
            s += j
            if s == n:
                cnt += 1
                break
            elif s > n:
                break
        


    
        
    
    print("#{}".format(k+1), cnt)