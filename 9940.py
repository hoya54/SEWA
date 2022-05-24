
t = int(input())



for k in range(t):
    n = int(input())

    lst = list(map(int, input().split()))

    ar = [0] + [1]*n

    for i in range(n):
        num = lst[i]
        ar[num] -= 1
    

    if min(ar) == max(ar) == 0:
        r = 'Yes'
    else:
        r = 'No'

        
    print("#{}".format(k+1), r)

