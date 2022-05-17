t = int(input())

dic = {'0001101': 0, 
       '0011001': 1, 
       '0010011': 2, 
       '0111101': 3, 
       '0100011': 4, 
       '0110001': 5, 
       '0101111': 6, 
       '0111011': 7, 
       '0110111': 8, 
       '0001011': 9}

for k in range(t):
    n, m = map(int, input().split())

    p = ""
    ar = []
    for _ in range(n):
        ar.append(list(input().rstrip()))

    for i in range(n):
        if '1' in ar[i]:
            p = ''.join(map(str, ar[i]))
            break
    
    rev = p[::-1]
    for i in range(m):
        if rev[i] == '1':
            rev = rev[i:i+56]
            break
    p = rev[::-1]

    lst = []
    for i in range(0, 56, 7):
        lst.append(dic[p[i:i+7]])
    
    odd = 0
    even = 0

    for i in range(7):
        if i%2 == 0:
            odd += lst[i]
        else:
            even += lst[i]
    r = odd*3 + even + lst[-1]

    result = 0
    if r%10 == 0:
        result = sum(lst)
    else:
        result = 0
    
    print("#{}".format(k+1), result)



