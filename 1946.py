t = int(input())

for k in range(t):
    n = int(input())

    lst = []

    for i in range(n):
        c, num = map(str, input().split())
        for j in range(int(num)):
            lst.append(c)
    
    print("#{}".format(k+1))
    for i in range(len(lst)):
        print(lst[i], end='')
        if i%10 == 9 or i+1 == len(lst):
            print()
    

