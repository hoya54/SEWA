n = int(input())

for j in range(n):
    st = list(map(int, input().split()))

    r = 0
    for i in range(10):
        r += st[i]
    
    r = round(r/10)
    print("#{}".format(j+1), r)