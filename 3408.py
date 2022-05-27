
t = int(input())


for k in range(t):
    n = int(input())

    s1 = n*(n+1)//2

    s2 = 2*s1-n

    s3 = 2*s1

    
    print("#{}".format(k+1), s1, s2, s3)