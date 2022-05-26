

t = int(input())


for k in range(t):
    n = int(input())

    cnt = 0
    lst = []
    while cnt < n:
        st = input().rstrip()

        cnt += st.count('.')
        cnt += st.count('?')
        cnt += st.count('!')

        lst += list(map(str, st.split()))
    
    r = []

    name = 0
    for word in lst:
        end = False

        if word[-1] in ['.', '?', '!']:
            end = True
            word = word[:-1]
        
        if 'A' <= word[0] <= 'Z':
            is_name = True
            for w in range(1, len(word)):
                if word[w] < 'a' or word[w] > 'z':
                    is_name = False
                    break
            if is_name:
                name += 1



        if end:
            r.append(name)
            name = 0
        
        



    
    
    print("#{}".format(k+1), ' '.join(map(str, r)))
