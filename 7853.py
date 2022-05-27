

t = int(input())

def func(lst, d):
    global s
    global st

    if d == len(st):
        s.add(''.join(map(str, lst)))
    
    else:
        if d+1 < len(st):
            func(lst+st[d+1], d+1)
        
        func(lst+st[d], d+1)
        func(lst+st[d-1], d+1)




for k in range(t):
    st = list(input().rstrip())

    s = set()
    
    d = 0
    lst =''

    
    func(lst + st[d], d+1)

    if d+1 < len(st):
        func(lst + st[d+1], d+1)

    print("#{}".format(k+1), len(s))