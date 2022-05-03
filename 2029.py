n = int(input())

for j in range(n):
    a, b = map(int, input().split())

    print("#{}".format(j+1), a//b, a%b)