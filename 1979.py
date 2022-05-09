t = int(input())

for r in range(t):
    n, k = map(int, input().split())

    ar = []
    ar.append([0]*(n+2))
    for _ in range(n):
        st = [0] + list(map(int, input().split())) + [0]
        ar.append(st)
    ar.append([0]*(n+2))

    lst = [0]*(n+1)

    for i in range(1, n+1):
        for j in range(1, n+1):
            right = 1
            down = 1

            if ar[i][j] == 1:
                if ar[i-1][j] != 1:
                    for w in range(i+1, n+1):
                        if ar[w][j] == 1:
                            down += 1
                        else:
                            break
                    lst[down] += 1

                if ar[i][j-1] != 1:
                    for w in range(j+1, n+1):
                        if ar[i][w] == 1:
                            right += 1
                        else:
                            break
                    lst[right] += 1

    print("#{}".format(r+1), lst[k])
