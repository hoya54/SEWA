
t = int(input())

for k in range(t):
    lst = list(map(int, input().split()))

    summ = 0
    for i in lst:
        if i < 40:
            summ += 40
        else:
            summ += i

    
    print("#{}".format(k+1), summ//len(lst))