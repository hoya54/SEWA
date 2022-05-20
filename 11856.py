
t = int(input())

for k in range(t):
    st = list(input().rstrip())
    
    r = ''
    st.sort()
    if st[0] == st[1] and st[2] == st[3] and st[1] != st[2]:
        r = 'Yes'
    else:
        r = 'No'
    
        
    
    print("#{}".format(k+1), r)