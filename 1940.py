t = int(input())

for k in range(t):
    n = int(input())

    distance = 0
    speed = 0
    for i in range(n):
        st = list(map(int, input().split()))

        if st[0] == 1:
            speed += st[1]
            distance += speed
        elif st[0] == 2:
            speed -= st[1]
            speed = max(0, speed)
            distance += speed
        else:
            distance += speed
        
    print("#{}".format(k+1), distance)