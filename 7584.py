
t = int(input())



for k in range(t):
    r = int(input())
    r = r-1
    n = 0
    while r >= 0:
        if r%2 == 1:
            r = (r-1)//2
        if r%4 == 0:
            n = 0
            break
        elif r%2 == 0:
            n = 1
            break
  
    print("#{}".format(k+1), n)
