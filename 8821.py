t = int(input())

for k in range(t):
    st = input().rstrip()
    
    lst = [0]*10

    for i in st:
        i = int(i)
        lst[i] = (lst[i]+1)%2
        

    print("#{}".format(k+1), sum(lst))




