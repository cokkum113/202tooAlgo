import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

lecture = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    lecture[a].append(b)
    cnt[b] += 1

que = deque()

for i in range(1, n + 1):
    if cnt[i] == 0:
        que.append([1, i])
    
stack = [0] * (n + 1)

while que:
    now, lec = que.popleft()
    stack[lec] = now
    for next in lecture[lec]:
        cnt[next] -= 1
        if cnt[next] == 0:
            que.append([now + 1, next])

for i in stack[1:]:
    print(i, end=' ')
    
