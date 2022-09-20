import sys
input = sys.stdin.readline
from itertools import combinations

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

t = int(input())
for _ in range(t):
    total = 0
    ll = list(map(int, input().split()))
    n = ll[0]
    ll = ll[1:]
    nums = list(combinations(ll, 2))
    for i in nums:
        maxi = max(i)
        mini = min(i)
        total += gcd(maxi, mini)
    
    print(total)