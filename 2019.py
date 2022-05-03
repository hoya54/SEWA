n = int(input())

r = []
b = 1
r.append(b)

for i in range(n):
    b *= 2
    r.append(b)

print(' '.join(map(str, r)))