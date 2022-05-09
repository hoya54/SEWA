t = int(input())

def func(ar):
    
    for i in range(9):
        test = [0]*10
        for j in range(9):
            if test[ar[i][j]] == 0:
                test[ar[i][j]] = 1
            else:
                return 0

    for j in range(9):
        test = [0]*10
        for i in range(9):
            if test[ar[i][j]] == 0:
                test[ar[i][j]] = 1
            else:
                return 0
    
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            test = [0]*10
            for x in range(3):
                for y in range(3):
                    if test[ar[i+x][j+y]] == 0:
                        test[ar[i+x][j+y]] = 1
                    else:
                        return 0
    
    return 1





for k in range(t):
    ar = []
    for _ in range(9):
        st = list(map(int, input().split()))
        ar.append(st)
    
    r = func(ar)

    print("#{}".format(k+1), r)
