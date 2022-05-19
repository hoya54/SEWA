

for k in range(10):
    n = int(input())

    lst = list(map(int, input().split()))

    lst.sort()
    for i in range(n):
        lst[0] += 1
        lst[-1] -= 1
        lst.sort()
    

    print("#{}".format(k+1), max(lst) - min(lst))




