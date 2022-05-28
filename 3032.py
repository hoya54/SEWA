
t = int(input())

def func(r1, r2, k):
    r = q = 1
    s = s1 =1
    s2=0
    t = t1 = 0
    t2 = 1
    tmp = r1

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        s = s1 - q * s2
        t = t1 - q * t2

        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t

    if r1 != 1:
        print("#{}".format(k+1), -1)
    else:
        print("#{}".format(k+1), s1, t1)

for k in range(t):
    a, b = map(int, input().split())

    func(a, b, k)
    
    
        
