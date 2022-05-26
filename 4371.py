
t = int(input())


for k in range(t):
    n = int(input())

    lst = []
    include = [0]*n
    include[0] = 1

    for i in range(n):
        lst.append(int(input()))
    
    ship = 0
    for i in range(1, len(lst)):
        if sum(include) == len(lst):
            break
        if include[i] == 1:
            continue
        
        include[i] = 1

        term = lst[i]-1

        last = lst[i]

        for j in range(i+1, len(lst)):
            if lst[j] == last + term:
                last = lst[j]
                include[j] = 1
            
            if lst[j] > last + term:
                break
        
        ship += 1
    
    print("#{}".format(k+1), ship)
    
