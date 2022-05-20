
t = int(input())

for k in range(t):
    n = int(input())
    lst = list(map(str, input().split()))

    left = []
    right = []
    n = len(lst)
    n = (n+1)//2

    left = lst[:n]
    right = lst[n:]
    
    r = []
    left = left[::-1]
    right = right[::-1]

    while left or right:
        if left:
            r.append(left.pop())
        if right:
            r.append(right.pop())
    
        
    
    print("#{}".format(k+1), ' '.join(map(str, r)))