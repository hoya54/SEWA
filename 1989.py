t = int(input())

for k in range(t):
    st = list(input())

    re = st[:]
    re.reverse()

    if st == re:
        print("#{}".format(k+1), 1)
    else:
        print("#{}".format(k+1), 0)