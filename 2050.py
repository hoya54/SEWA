
st = input().rstrip()

r = []
for s in st:
    r.append(ord(s)-64)

print(' '.join(map(str, r)))