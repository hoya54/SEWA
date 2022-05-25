
t = int(input())


for k in range(t):
    n = int(input())

    lst = list(map(int, input().split()))

    while len(lst) != n:
        temp = list(map(int, input().split()))
        lst += temp

    st = ''.join(map(str, lst))
    
    for i in range(999999):
        i = str(i)

        if i not in st:
            print("#{}".format(k+1), i)
            break
