
t = int(input())

for k in range(t):
    n = int(input())

    lst = input().rstrip()
    lst1 = input().rstrip()

    cnt = 0

    for i in range(len(lst)):
        if lst[i] == lst1[i]:
            cnt += 1


    


    print("#{}".format(k+1), cnt)