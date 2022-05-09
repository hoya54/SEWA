
t = int(input())

for k in range(t):
    p, q, r, s, w = map(int, input().split())

    A = p*w
    B = 0
    if w <= r:
        B = q
    else:
        B = q
        w -= r
        B += w*s
    
    print("#{}".format(k+1), min(A, B))
