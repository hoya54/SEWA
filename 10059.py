
t = int(input())


for k in range(t):
    st = input().rstrip()

    l = int(st[:2])
    r = int(st[2:])

    lm = True
    rm = True
    if 1 <= l <= 12:
        lm = True
    else:
        lm = False

    if 1 <= r <= 12:
        rm = True
    else:
        rm = False
    
    r = ''
    if lm and rm:
        r = 'AMBIGUOUS'
    elif lm:
        r = 'MMYY'
    elif rm:
        r = 'YYMM'
    else:
        r = 'NA'


    
    print("#{}".format(k+1), r)