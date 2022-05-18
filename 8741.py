t = int(input())

for k in range(t):
    lst = list(map(str, input().split()))

    r = ''
    for i in lst:
        r += i[0]
    
    r = r.upper()
    
    print("#{}".format(k+1), r)




