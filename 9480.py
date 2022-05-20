from itertools import combinations

t = int(input())

for k in range(t):
    n = int(input())

    cnt = 0
    lst = []

    for i in range(n):
        st = input().rstrip()
        temp = [0]*26
        for j in range(len(st)):
            temp[ord(st[j])-97] += 1
        lst.append(temp)
    
    for i in range(1, n+1):
        for j in combinations(lst, i):
            temp = [0]*26
            for p in range(len(j)):
                for e in range(26):
                    temp[e] += j[p][e]
            flag = True
            for p in range(26):
                if temp[p] == 0:
                    flag = False
                    break
            if flag:
                cnt += 1



        
    
    print("#{}".format(k+1), cnt)