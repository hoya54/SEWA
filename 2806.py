t = int(input())

def func(ar, d, n):
    global cnt

    if d == n:
        cnt += 1
        #print(ar)
        return
    
    for i in range(n):
        if promising(ar, i, d):
            temp = ar[:]
            temp[d] = i
            func(temp, d+1, n)

    

def promising(ar, i, d):
    flag = True

    for j in range(d):
        if i == ar[j]:
            flag = False
            break
        if abs(i - ar[j]) == abs(d-j):
            flag = False
            break
    
    return flag
    

for k in range(t):
    n = int(input())

    cnt = 0
    ar = [0]*n

    func(ar, 0, n)
    
    print("#{}".format(k+1), cnt)

    

        
        


