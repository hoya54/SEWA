
t = int(input())

for k in range(t):
    st = input().rstrip()
    n = len(st)
    j = 0
    
    ar = [[ '.' for _ in range(5+4*(n-1))] for _ in range(5)]

    for i in range(2, 2+(n-1)*4 +1, 4):
        ar[2][i] = st[j]
        j += 1
        ar[0][i] = '#'
        ar[1][i-1] = ar[1][i+1] = '#'
        ar[2][i-2] = ar[2][i+2] = '#'
        ar[3][i-1] = ar[3][i+1] = '#'
        ar[4][i] = '#'
    
    for i in range(5):
        print(''.join(map(str, ar[i])))
