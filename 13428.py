t = int(input())


for k in range(t):
    st = int(input())

    lst = []
    
    temp = list(str(st))
    lst.append(st)

    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if temp[i] == temp[j]:
                continue
            else:
                s = temp[:]
                s[i], s[j] = s[j], s[i]
                
                if s[0] != '0':
                    s = ''.join(map(str, s))
                    lst.append(int(s))
    
    print("#{}".format(k+1), min(lst), max(lst))


