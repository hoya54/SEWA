t = int(input())

for k in range(t):
    st = input().rstrip()
    st = st.replace('p', 'Q')
    st = st.replace('q', 'P')
    st = st.replace('b', 'D')
    st = st.replace('d', 'B')

    st = st.replace('Q', 'q')
    st = st.replace('P', 'p')
    st = st.replace('D', 'd')
    st = st.replace('B', 'b')

    print("#{}".format(k+1), st[::-1])




