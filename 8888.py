
t = int(input())


for k in range(t):
    n, m, p = map(int, input().split())

    lst = []
    score = [0]*m
    
    for i in range(n):
        st = list(map(int, input().split()))
        lst.append(st)
    
    for i in range(m):
        s = 0

        for j in range(n):
            if lst[j][i] == 0:
                s += 1
        
        score[i] = s
    
    total = []

    for i in range(len(lst)):
        many = sum(lst[i])
        value = 0
        for j in range(m):
            value += lst[i][j]*score[j]
        
        total.append([many, value])
    
    sumscore = []
    #print(total)
    for i in range(len(total)):
        mymany = total[i][0]
        myscore = total[i][1]

        x1, x2, x3 = 0, 0, 0


        for j in range(len(total)):
            if i == j:
                continue
                
            if total[j][1] > myscore:
                x1 += 1
            
            if total[j][1] == myscore and total[j][0] > mymany:
                x2 += 1
            
            if total[j][1] == myscore and total[j][0] == mymany and j < i:
                x3 += 1
                
            
        sumscore.append(x1+x2+x3+1)
    
    


    
    print("#{}".format(k+1), total[p-1][1], sumscore[p-1])