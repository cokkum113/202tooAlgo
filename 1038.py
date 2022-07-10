import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
ans = []
for i in range(1, 11):
    for c in combinations(range(0, 10), i):
        combi = list(c)
        combi.sort(reverse=True)
        ans.append(int("".join(map(str, combi))))
    
ans.sort()
if n >=  1023:
    print(-1)
else:
    print(ans[n])