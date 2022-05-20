
t = int(input())

for k in range(t):
    st = list(input().rstrip())

    st.sort()

    dic = {}

    for i in st:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    r = ''
    for c, i in dic.items():
        if i%2 == 1:
            r += c
       
    if r == '':
        print("#{}".format(k+1), 'Good')
    else:
        print("#{}".format(k+1), r)