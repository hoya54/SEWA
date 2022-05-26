

t = int(input())

def func(d, s, n):
    global maxx

    if d < n:
        maxx = max(maxx, s*lst[d])
        func(d+1, s*lst[d], n)

        maxx = max(maxx, s+lst[d])
        func(d+1, s+lst[d], n)


for k in range(t):
    n = int(input())

    lst = list(map(int, input().split()))

    maxx = lst[0]

    func(1, lst[0], n)




    

    
    
    print("#{}".format(k+1), maxx)
