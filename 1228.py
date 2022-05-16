
for k in range(10):
    n = int(input())

    lst = list(map(str, input().split()))

    c = int(input())

    i = 0
    count = 0
    c_lst = list(map(str, input().split()))
    while True:
        if c_lst[i] =='I':
            i += 1

            x = int(c_lst[i])
            i += 1

            y = int(c_lst[i])
            i += 1

            for j in range(y):
                num = c_lst[i]
                i += 1

                lst.insert(x, num)
                x += 1

            count += 1

        if count == c:
            break
    
    print("#{}".format(k+1), ' '.join(map(str, lst[:10])))