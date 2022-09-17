import sys
input = sys.stdin.readline
from collections import deque

u, v = map(int, input().split())

leaf = [[] for _ in range(u + 1)]

tree = [[] for _ in range(u + 1)]

visited = [False] * (u + 1)

def bfs(x):
    que = deque()
    que.append(x)
    visited[x] = True

    while que:
        xx = que.popleft()
        for nx in tree[xx]:
            if not visited[nx]:
                que.append(nx)
                visited[nx] = True
                leaf[xx].append(nx)

for _ in range(u - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
bfs(1)

cnt = 0
for i in range(1, len(leaf)):
    if len(leaf[i]) == 0:
        cnt += 1

print(v/cnt)

