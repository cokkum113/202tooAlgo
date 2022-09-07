import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

que = deque()

for i in range(n):
    que.append(i + 1)

aa = []
cnt = 0
while que:
    cnt += 1
    if cnt % k == 0:
        x = que.popleft()
        aa.append(str(x))
        
    else:
        x = que.popleft()
        que.append(x)


print("<", end='')
print(", ".join(aa),">", sep="")