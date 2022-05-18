t = int(input())

for k in range(t):
    p, q = map(float, input().split())

    r = ''
    s1 = (1-p)*q
    s2 = p*(1-q)*q

    if s1 < s2:
        r = 'YES'
    else:
        r = 'NO'
    
    print("#{}".format(k+1), r)




