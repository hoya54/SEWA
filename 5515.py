t = int(input())

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for k in range(t):
    m, d = map(int, input().split())

    days = 0
    for i in range(1, m):
        days += month[i]

    days += d

    
    
    print("#{}".format(k+1), (days+3) %7)
    



