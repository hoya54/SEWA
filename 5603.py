
t = int(input())


for k in range(t):
    n = int(input())

    lst = []
    for i in range(n):
        s = int(input())
        lst.append(s)

    avg = sum(lst)//n

    cnt = 0
    for i in lst:
        cnt += abs(avg - i)
    

    print("#{}".format(k+1), cnt//2)

# for i in range(1, 10001):
#     print(dic[i])