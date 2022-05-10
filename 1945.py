t = int(input())

d = [2, 3, 5, 7, 11]

for k in range(t):
    n = int(input())

    r = []
    t = n
    for m in d:
        cnt = 0
        while t > 0:
            if t%m == 0:
                t /= m
                cnt += 1
            else:
                break
        r.append(cnt)
    print("#{}".format(k+1), ' '.join(map(str, r)))
