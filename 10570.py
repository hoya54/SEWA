import math

t = int(input())

for k in range(t):

    a, b = map(int, input().split())

    cnt = 0
    for i in range(a, b+1):
        st = list(str(i))
        r = math.sqrt(i)

        if r != int(r):
            continue
        
        r = list(str(int(r)))

        if st == st[::-1] and r == r[::-1]:
            cnt += 1

    print("#{}".format(k+1), cnt)