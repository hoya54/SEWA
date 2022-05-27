

t = int(input())


for k in range(t):
    n = int(input())

    left = 1
    right = 1

    l = 1
    r = 3
    for i in range(2, n+1):
        left += l
        right += r

        l += 2
        r += 2
    
    print("#{}".format(k+1), left*2-1, right*2-1)