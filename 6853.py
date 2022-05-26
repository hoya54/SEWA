
t = int(input())


for k in range(t):
    
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input())

    lst = [0, 0, 0]
    for i in range(n):
        x, y = map(int, input().split())

        if x1 < x < x2 and y1 < y < y2:
            lst[0] += 1
        elif x < x1 or x > x2 or y < y1 or y > y2:
            lst[2] += 1
        else:
            lst[1] += 1
    


    
    print("#{}".format(k+1), lst[0], lst[1], lst[2])
    
