t = int(input())

def inorder(lst, i, n):
    global ar

    if i*2+1 < n:
        inorder(lst, i*2+1, n)
    ar[i] = lst.pop()
    if i*2+2 < n:
        inorder(lst, i*2+2, n)

for k in range(t):
    d = int(input())
    
    lst = list(map(int, input().split()))
    lst.reverse()

    n = len(lst)

    ar = [0]*(len(lst))

    inorder(lst, 0, n)
    
    
    s = 1
    print("#{}".format(k+1), ar[0])
    for i in range(1, d):
        print(' '.join(map(str, ar[s:s+2**i])))
        s = s+2**i



