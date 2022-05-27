

t = int(input())


r = []
for k in range(t):
    n = int(input())

    while n >= 10:
        n = sum(list(map(int, str(n))))

        



    r.append(n)

for i in range(len(r)):
    print("#{}".format(i+1), r[i])