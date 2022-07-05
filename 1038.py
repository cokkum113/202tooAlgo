import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
ans = []

for i in range(1, 11):
    for c in combinations(range(0, 10), i):
        xx = list(c)
        xx.sort(reverse=True)
        ans.append(int(''.join(map(str, xx))))
    
ans.sort()
try:
    print(ans[n])
except:
    print(-1)