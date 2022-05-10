t = int(input())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for j in range(t):
    n, k = map(int, input().split())

    lst = []
    for s in range(n):
        m, f, a = map(int, input().split())
        score = m*35+f*45+a*20
        lst.append([score, s+1])
    
    lst.sort(reverse=True)

    score = -1
    term = n//10
    for i in range(n):
        if i%term == 0:
            score += 1
        if lst[i][1] == k:
            break
    
    print("#{}".format(j+1), grade[score])
    
