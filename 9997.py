
t = int(input())

for k in range(t):
    a = int(input())

    print("#{}".format(k+1), a*2//60, a*2%60)