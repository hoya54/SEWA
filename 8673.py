from collections import deque

t = int(input())

for k in range(t):
    n = int(input())

    lst = list(map(int, input().split()))

    lst = deque(lst)

    s = 0
    for i in range(n, 0, -1):
        for j in range(2**(i-1)):
            a = lst.popleft()
            b = lst.popleft()

            s += abs(a-b)
            lst.append(max(a, b))


    print("#{}".format(k+1), s)