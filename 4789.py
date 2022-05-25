
t = int(input())


for k in range(t):
    st = input().rstrip()

    
    lst = []
    for i in st:
        n = int(i)
        lst.append(n)

    temp = lst[0]

    for i in range(len(lst)):
        lst[0] += i

        s = 0
        for i in range(1, len(lst)):
            if s >= i-1:

            s += lst[i]
    

    
        lst[0] = temp


    

    print("#{}".format(k+1), i)

