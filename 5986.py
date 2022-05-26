
t = int(input())

prime = [True]*1000
p = []
for i in range(2, 1000):
    if prime[i] == True:
        p.append(i)
        for j in range(i+i, 1000, i):
            prime[j] = False

for k in range(t):
    
    n = int(input())

    r = 0
    for i in range(len(p)):
        for j in range(i, len(p)):
            for e in range(j, len(p)):
                if p[i]+p[j]+p[e] == n:
                    r += 1
    
    
    print("#{}".format(k+1), r)
    
