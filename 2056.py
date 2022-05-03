
n = int(input())

m30 = [4, 6, 9, 11]
m31 = [1, 3, 5, 7, 8, 10, 12]

for i in range(n):
    st = input().rstrip()

    year = st[:4]
    month = st[4:6]
    day = st[6:]

    if 1<=int(month)<=12:
        pass
    else:
        print("#{}".format(i+1), -1)
        continue

    if int(month) == 2:
        if 1<=int(day)<=28:
            print("#{} {}/{}/{}".format(i+1, year, month, day))
        else:
            print("#{}".format(i+1), -1)
            continue
    elif int(month) in m30:
        if 1<=int(day)<=30:
            print("#{} {}/{}/{}".format(i+1, year, month, day))
        else:
            print("#{}".format(i+1), -1)
            continue
    else:
        if 1<=int(day)<=31:
            print("#{} {}/{}/{}".format(i+1, year, month, day))
        else:
            print("#{}".format(i+1), -1)
            continue
