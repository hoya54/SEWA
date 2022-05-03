T = int(input())

for j in range(T):
    n = int(input())
    lst = list(map(int, input().split()))

    maxx = lst[-1]

    summ = 0

    for i in range(n-2, -1, -1):

        if lst[i] < maxx:
            summ += (maxx-lst[i])
        else:
            maxx = lst[i]
    
    print("#{} {}".format(j+1, summ))