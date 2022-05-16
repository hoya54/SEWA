t = int(input())

for k in range(t):
    n = int(input())

    lst = []
    for i in range(n):
        lst.append("1/{}".format(n))

    print("#{}".format(k+1), ' '.join(map(str, lst)))