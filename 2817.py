
t = int(input())

def func(s, d, K):
    global cnt


    if d == n:
        if s == K:
            cnt += 1
    elif d < n:
        if s + lst[d] <= K:
            func(s+lst[d], d+1, K)

        func(s, d+1, K)

        


for k in range(t):
    n, K = map(int, input().split())

    lst = list(map(int, input().split()))

    cnt = 0

    func(0, 0, K)
        
    print("#{}".format(k+1), cnt)

