n = int(input())

for j in range(n):
    a, b = map(int, input().split())
    r = 0

    if a > b:
        r = '>'
    elif a < b:
        r = '<'
    else:
        r = '='
        
    print("#{}".format(j+1), r)