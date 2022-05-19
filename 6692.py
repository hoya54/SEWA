
t = int(input())
for k in range(t):
    n = int(input())

    r = 0
    for i in range(n):

        a, b = map(float, input().split())
        r += a*b
    

    print("#{} {:.6f}".format(k+1, r))
    



