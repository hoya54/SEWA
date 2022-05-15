t = int(input())

a = {"SUN":7, "MON":6, "TUE":5, "WED":4, "THU":3, "FRI":2, "SAT":1}
for k in range(t):
    st = input()
    print("#{}".format(k+1), a[st])
