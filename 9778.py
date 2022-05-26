

t = int(input())


for k in range(t):
    
    n = int(input())

    card = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]

    s = 0
    for _ in range(n):
        c = int(input())
        card[c] -= 1
        s += c
    
    over = 0
    
    for i in range(2, 12):
        if s + i > 21:
            over += card[i]
    
    little = sum(card) - over


    r = ''
    if over >= little:
        r = 'STOP'
    else:
        r = 'GAZUA'

    

    
    
    print("#{}".format(k+1), r)
