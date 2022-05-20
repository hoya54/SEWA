
t = int(input())

for k in range(t):
    s, e, m = map(int, input().split())

    i=1
    S, E, M = 1, 1, 1
    while True:
        if (s, e, m) == (S, E, M):
            break

        
        S += 1
        if S == 366:
            S = 1
        
        E += 1
        if E == 25:
            E = 1
        
        M += 1
        if M == 30:
            M = 1

        i += 1

        
    
    print("#{}".format(k+1), i)