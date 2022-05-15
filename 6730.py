t = int(input())

for k in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    max_up = 0
    max_down = 0

    for i in range(1, n):
        d = lst[i] - lst[i-1]

        if d > 0:
            up = d
            max_up = max(up, max_up)
        else:
            down = -d
            max_down = max(down, max_down)
    
    print("#{}".format(k+1), max_up, max_down)