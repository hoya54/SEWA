from itertools import combinations

t = int(input())


for k in range(t):
    num = input().rstrip()
    col = input().rstrip()

    r = 'Continue'

    lst = []
    for i in range(9):
        lst.append((int(num[i]), col[i], i))
    
    for x1 in combinations(lst, 3):
        temp  = []
        if not (x1[0][1] == x1[1][1] == x1[2][1]):
            continue
        q = [x1[0][0], x1[1][0], x1[2][0]]
        q.sort()
        if (x1[0][0] == x1[1][0] == x1[2][0]) or (q[0]+1 == q[1] == q[2]-1):
            pass
        else:
            continue

        for e in lst:
            if e not in x1:
                temp.append(e)

        for x2 in combinations(temp, 3):
            if not (x2[0][1] == x2[1][1] == x2[2][1]):
                continue
            q = [x2[0][0], x2[1][0], x2[2][0]]
            q.sort()
            if (x2[0][0] == x2[1][0] == x2[2][0]) or (q[0]+1 == q[1] == q[2]-1):
                pass
            else:
                continue
            
            x3 = []
            for w in temp:
                if w not in x2:
                    x3.append(w)

            if not (x3[0][1] == x3[1][1] == x3[2][1]):
                continue
            q = [x3[0][0], x3[1][0], x3[2][0]]
            q.sort()
            if (x3[0][0] == x3[1][0] == x3[2][0]) or (q[0]+1 == q[1] == q[2]-1):
                pass
            else:
                continue

            r = 'Win'
            break
        if r == 'Win':
            break


    
    print("#{}".format(k+1), r)