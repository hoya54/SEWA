
t = int(input())

ar = [[0 for _ in range(301)] for _ in range(301)]
dic = {}

s = 1
for i in range(1, 301):
    a, b = 1, i
    for j in range(i):
        ar[a][b] = s
        dic[s] = (a, b)
        s += 1
        a, b = a+1, b-1

for k in range(t):
    x, y = map(int, input().split())

    x1, y1, x2, y2 = dic[x][0], dic[x][1], dic[y][0], dic[y][1]
    
    x3, y3 = x1+x2, y1+y2

    print("#{}".format(k+1), ar[x3][y3])

# for i in range(1, 10001):
#     print(dic[i])