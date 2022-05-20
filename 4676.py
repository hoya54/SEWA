
t = int(input())

for k in range(t):
    st = list(input().rstrip())
    n = int(input())

    ar = [0]*(len(st)+1)
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    for i in lst:
        st.insert(i, '-')

    print("#{}".format(k+1), ''.join(map(str, st)))
    