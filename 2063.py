n = int(input())


st = list(map(int, input().split()))

st.sort()
print(st[(n+1)//2-1])