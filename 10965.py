from collections import deque

p = [True]*int(10000000 ** 0.5)
prime = []
for i in range(2, int(10000000 ** 0.5)):
    if p[i] == True:
        prime.append(i)
        for j in range(i+i, int(10000000 ** 0.5), i):
            p[j] = False

t = int(input())
r = []

for k in range(t):
    n = int(input())

    if n == 1:
        r.append(1)
        continue
    elif n in prime:
        r.append(n)
        continue

    lst = []
    root = n
    i = 0

    while n > 1:
        #print(n)
        if n%prime[i] != 0:
            i += 1
        else:
            n = n//prime[i]
            lst.append(prime[i])
        
        if i >= len(prime):
            lst.append(n)
            break
           

    lst.sort()
    lst = deque(lst)

    mul = 1
    i = 0
    #print(lst)
    while lst:
        if len(lst) > 1:
            if lst[0] != lst[1]:
                mul *= lst.popleft()
            else:
                lst.popleft()
                lst.popleft()   
        elif len(lst) == 1:
            mul *= lst.popleft()
        else:
            break

    r.append(mul)


for i in range(t):
    print("#{}".format(i+1), r[i])