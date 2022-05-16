
t = int(input())

for k in range(t):
    lst = list(map(str, input().split()))

    r = []
    for i in lst:
        s = 0
        for j in range(len(i)):
            s += int(i[j])
        r.append(s)
    


    print("#{}".format(k+1), max(r), min(r))