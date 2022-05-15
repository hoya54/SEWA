t = int(input())

for k in range(t):
    st = input().rstrip()
    cnt = 0

    for i in range(len(st)):
        if st[i] == 'x':
            cnt += 1
    if cnt >= 8:
        print("#{}".format(k+1), 'NO')
    else:
        print("#{}".format(k+1), 'YES')