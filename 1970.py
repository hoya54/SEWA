t = int(input())

for k in range(t):
    n = int(input())

    print("#{}".format(k+1))
    print(n//50000, end=' ')
    n %= 50000

    print(n//10000, end=' ')
    n %= 10000

    print(n//5000, end=' ')
    n %= 5000

    print(n//1000, end=' ')
    n %= 1000

    print(n//500, end=' ')
    n %= 500

    print(n//100, end=' ')
    n %= 100

    print(n//50, end=' ')
    n %= 50

    print(n//10)
    