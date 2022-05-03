n = int(input())

r = []

for i in range(n, -1, -1):
    r.append(i)
    
print(' '.join(map(str, r)))