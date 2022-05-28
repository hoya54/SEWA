

t = int(input())


for k in range(t):
    p = input().rstrip()
    q = input().rstrip()

    r = 'Y'
    if p+'a' < q:
        r = 'Y'
    else:
        r = 'N'



    print("#{}".format(k+1), r)