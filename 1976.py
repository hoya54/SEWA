t = int(input())

for k in range(t):
    h1, m1, h2, m2 = map(int, input().split())

    m = m1+m2

    h = m//60
    h += (h1+h2)
    if h > 12:
        h = (h-1) % 12 + 1
        
    m = m%60 

    print("#{}".format(k+1), h, m)