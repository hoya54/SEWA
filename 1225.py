from collections import deque

for k in range(10):
    t = int(input())
    lst = list(map(int, input().split()))

    lst = deque(lst)

    i = 1
    while True:
        if i > 5:
            i = 1

        t = lst.popleft()

        t -= i
        i += 1

        if t <= 0:
            lst.append(0)
            break

        lst.append(t)



    print("#{}".format(k+1), ' '.join(map(str, list(lst))))