
t = int(input())

d = {"ZRO":0,
     "ONE":1,
     "TWO":2,
     "THR":3,
     "FOR":4,
     "FIV":5,
     "SIX":6,
     "SVN":7,
     "EGT":8,
     "NIN":9}

c = {0:"ZRO",
     1:"ONE",
     2:"TWO",
     3:"THR",
     4:"FOR",
     5:"FIV",
     6:"SIX",
     7:"SVN",
     8:"EGT",
     9:"NIN"}

for k in range(t):
    x, n = map(str, input().split())
    n = int(n)

    lst = list(map(str, input().split()))

    for i in range(len(lst)):
        lst[i] = d[lst[i]]
    lst.sort()

    for i in range(len(lst)):
        lst[i] = c[lst[i]]
    
    
    print("#{}".format(k+1))
    print(' '.join(map(str, lst)))
