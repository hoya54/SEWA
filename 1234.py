
for k in range(10):
    lst = list(map(str, input().split()))

    n = lst[0]
    lst = list(lst[1])

    while True:
        state = 0
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                del lst[i]
                del lst[i]
                state = 1
                break

        if state == 0:
            break
    


    print("#{}".format(k+1), ''.join(map(str, lst)))