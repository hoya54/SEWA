
t = int(input())

lst=[0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0]*90

for i in range(11, 101):
    lst[i] = lst[i-1] + lst[i-5]

for k in range(t):
    n = int(input())

        
    print("#{}".format(k+1), lst[n])

