

t = int(input())

result = []

for k in range(t):
    a, b, c, d = map(int, input().split())

    r = ''
    if a/b > c/d:
        r = 'ALICE'
    elif a/b < c/d:
        r = 'BOB'
    else:
        r = 'DRAW'
    
    result.append(r)

for i in range(len(result)):
    print("#{}".format(i+1), result[i])
