
t = int(input())

def func(x):
    x = str(x)
    for i in range(1, len(x)):
        if x[i-1] > x[i]:
            return False
    
    return True

for k in range(t):
    n = int(input())

    lst = list(map(int, input().split()))

    lst.sort(reverse=True)
    maxx = -1

    for i in range(n):
        for j in range(i+1, n):
            if func(lst[i]*lst[j]):
                maxx = max(maxx, lst[i]*lst[j])
        
    
    print("#{}".format(k+1), maxx)