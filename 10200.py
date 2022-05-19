t = int(input())

for k in range(t):
    n, a, b = map(int, input().split())


    
    print("#{}".format(k+1), min(a, b), max(a+b-n, 0))


