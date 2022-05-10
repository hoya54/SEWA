end = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

t = int(input())

for k in range(t):
    m1, d1, m2, d2 = map(int, input().split())

    day = 0
    for m in range(m1, m2+1):
        if m == m1:
            day += (end[m] - d1 + 1)
            continue
        if m == m2:
            day += d2
            continue
        
        day += end[m]
    
    print("#{}".format(k+1), day)

