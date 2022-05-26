
t = int(input())


for k in range(t):
    st = input().rstrip()

    
    lst = [0]
    for i in st:
        n = int(i)
        lst.append(n)

    temp = lst[0]

    r = 0
    for i in range(len(lst)):
        lst[0] += i

        s = lst[0]
        flag = False
        for j in range(1, len(lst)):
            if s >= j-1:
                s += lst[j]

                if j == len(lst)-1:
                    r = i
                    flag = True
            else:
                break
        if flag:
            break

        lst[0] = temp

    print("#{}".format(k+1), r)

