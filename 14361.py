from itertools import permutations


t = int(input())

for k in range(t):
    
    on = int(input())

    n = str(on)

    n = list(n)

    lst = []

    for i in n:
        num = int(i)

        lst.append(num)
    
    r = False

    for i in permutations(lst, len(lst)):
        if i[0] == 0:
            continue
        
        temp = int(''.join(map(str, list(i))))
        if temp%on == 0 and temp != on:
            r = True
            break
    
    if r == True:
        r = 'possible'
    else:
        r = 'impossible'

    print("#{}".format(k+1), r)
