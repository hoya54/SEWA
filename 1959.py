t = int(input())

for k in range(t):
    n, m = map(int, input().split())

    short = list(map(int, input().split()))

    long = list(map(int, input().split()))

    if len(short) > len(long):
        short, long = long, short
    
    maxx = 0
    
    
    for i in range(len(long)-len(short)+1):
        sum = 0
        for j in range(len(short)):
            sum += (long[i+j]*short[j])
        maxx = max(maxx, sum)
    
    print("#{}".format(k+1), maxx)
