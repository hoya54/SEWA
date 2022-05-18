t = int(input())

for k in range(t):
    n = int(input())
    
    r = ''
    if n%2 == 0:
        r = 'Even'
    else:
        r = 'Odd'

    print("#{}".format(k+1), r)




