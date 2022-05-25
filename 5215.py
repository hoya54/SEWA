
t = int(input())

def func(d, s, c, limit):
    global maxx

    if d < n:
        score, cal = lst[d][0], lst[d][1]
        if c + cal <= limit:
            maxx = max(maxx, s + score)
            func(d+1, s+score, c+cal, limit)
        
        maxx = max(maxx, s)
        func(d+1, s, c, limit)


for k in range(t):
    n, limit = map(int, input().split())

    lst = []
    for i in range(n):
        score, cal = map(int, input().split())
        lst.append((score, cal))

    maxx = 0
    d = 0
    
    score, cal = lst[d][0], lst[d][1]
    if cal <= limit:
        maxx = max(maxx, score)
        func(d+1, score, cal, limit)

    maxx = max(maxx, score)
    func(d+1, 0, 0, limit)
        

    print("#{}".format(k+1), maxx)

