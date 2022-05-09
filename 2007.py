t = int(input())

for k in range(t):
    st = input()

    for i in range(1, 11):
        pattern = st[:i+1]
        if pattern == st[i: 2*i+1]:
            print("#{}".format(k+1), i)
            break
    