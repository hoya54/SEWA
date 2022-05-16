
t = int(input())

for k in range(t):
    n = input().rstrip()

    s = '1'
    cnt = 0
    for i in range(len(n)):
        if n[i] == s:
            cnt += 1
            s = str((int(s)+1)%2)
        else:
            continue

    print("#{}".format(k+1), cnt)