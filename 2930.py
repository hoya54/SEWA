import heapq

t = int(input())


for k in range(t):
    n = int(input())

    h = []
    r = []

    for _ in range(n):
        com = list(map(int, input().split()))
    

        if com[0] == 1:
            heapq.heappush(h, (-com[1], com[1]))
        else:
            if not h:
                r.append(-1)
            else:
                d = heapq.heappop(h)[1]
                r.append(d)

    
    

    print("#{}".format(k+1), ' '.join(map(str, r)))