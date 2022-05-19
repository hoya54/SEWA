t = int(input())

for k in range(t):
    n= int(input())

    lst = []
    for i in range(n):
        st = int(input())

        if st == 0:
            lst.pop()
        else:
            lst.append(st)

    print("#{}".format(k+1), sum(lst))




