import math

t = int(input())

re = []
for k in range(t):
    n = int(input())

    score = 0

    for i in range(n):
        x, y = map(int, input().split())
    
        r = math.ceil(math.sqrt(x**2 + y**2)/20)

        if r <= 0:
            score += 10
        elif r <= 11:
            score += 11-r

    re.append(score)

        
for k in range(t):
    print("#{}".format(k+1), re[k])