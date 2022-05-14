t = int(input())

for k in range(t):
    n, d = map(int, input().split())

    d = 2*d+1

    if n%d == 0:
        n = n//d
    else:
        n = n//d + 1
    
    print("#{}".format(k+1), n)