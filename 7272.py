
t = int(input())

o = ['A','D','O','P','Q','R']

for k in range(t):
    
    x, y = map(str, input().split())

    r = 'SAME'
    if len(x) != len(y):
        r = 'DIFF'
    else:
        flag = True
        for i in range(len(x)):
            sx = 0
            sy = 0

            if x[i] in o:
                sx = 1
            elif x[i] == 'B':
                sx = 2
            else:
                sx = 0
            
            if y[i] in o:
                sy = 1
            elif y[i] == 'B':
                sy = 2
            else:
                sy = 0
            
            if sx != sy:
                r = 'DIFF'
                break
        
    
    print("#{}".format(k+1), r)
    
