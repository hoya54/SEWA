t = int(input())

for k in range(t):
    n = int(input())

    i=n
    num = [0]*10

    while True:
        t = str(i)

        for j in range(len(t)):
            if num[int(t[j])] == 0:
                num[int(t[j])] += 1

        if sum(num) == 10:
            print("#{}".format(k+1), i)
            break

        i += n


