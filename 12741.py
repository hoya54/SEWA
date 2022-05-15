t = int(input())

r = []
for k in range(t):
    a, b, c, d = map(int, input().split())

    lst = [0]*101

    left = max(a, c)
    right = min(b, d)

    if left < right:
        r.append(right - left)
    else:
        r.append(0)

for i in range(len(r)):
    print("#{}".format(i+1), r[i])
