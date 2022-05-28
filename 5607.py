from math import factorial
import sys

sys.setrecursionlimit(10000000)


t = int(input())

def pow(a, b):
    if b == 0:
        return 1
    ans = pow(a, b//2)
    next = (ans*ans)%1234567891
    if b%2 == 0:
        return next
    else:
        return (next*a)%1234567891


for k in range(t):
    n, r = map(int, input().split())
    
    ans = (factorial(n) * pow((factorial(r)*factorial(n-r))%1234567891, 1234567891-2))%1234567891

    print("#{}".format(k+1), ans)
