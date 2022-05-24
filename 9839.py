from itertools import combinations

t = int(input())


for k in range(t):
    n = int(input())

    lst = list(map(int, input().split()))

    bench = []

    for x, y in combinations(lst, 2):
        s = x*y
        s = str(s)
        
        ans = s[0]

        for i in range(len(s)-1):
            ans += str(int(ans[-1])+1)
        
        if ans == s:
            bench.append(int(s))
    
    if bench: 
        print("#{}".format(k+1), max(bench))
    else:
        print("#{}".format(k+1), -1)

