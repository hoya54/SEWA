t = int(input())

def func(lst, n):
    i = 1
    days = 0
    while True:
        for j in range(7):
            if lst[j] == 1:
                days += 1
                if days == n:
                    return i
            i += 1


for k in range(t):
    n = int(input())
    temp = list(map(int, input().split()))
    
    lst = []
    gar = 0
    for i in range(7):
        if temp[i] == 0:
            gar += 1
        else:
            tempo = temp[i:]
            for e in range(i):
                tempo.append(temp[e])
            lst.append(tempo)

    minn = 999999999

    for i in range(len(lst)):
        minn = min(func(lst[i], n), minn)
    print("#{}".format(k+1), minn)
    