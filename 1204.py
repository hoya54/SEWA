T = int(input())

for j in range(T):
    s = int(input())

    scores = [0]*101

    lst = list(map(int, input().split()))

    for i in lst:
        scores[i] += 1

    maxx = max(scores)

    result = []
    for i in range(0, 101):
        if scores[i] == maxx:
            result.append(i)
    
    print("#{} {}".format(s, max(result)))
    