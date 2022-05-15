t = int(input())

a = ['a', 'e', 'i', 'o', 'u']

for k in range(t):
    st = input().rstrip()

    r = ""
    for i in st:
        if i not in a:
            r += i
    
    print("#{}".format(k+1), r)