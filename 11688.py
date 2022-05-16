
t = int(input())

for k in range(t):
    st = input().rstrip()

    a = 1
    b = 1
    for i in range(len(st)):
        if st[i] == 'L':
            a = a
            b = a+b
        else:
            a = a+b
            b = b

    
    print("#{}".format(k+1), a, b)