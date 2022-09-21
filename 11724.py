import sys
input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())

graph = [[i] for i in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(x):
    que = deque()
    que.append(x)
    visited[x] = True

    while que:
        xx = que.popleft()
        for nx in graph[xx]:
            if not visited[nx]:
                visited[nx] = True
                que.append(nx)
    
ans = 0
for i in graph:
    for j in i:
        if not visited[j]:
            bfs(j)
            ans += 1
            visited[j] = True

print(ans - 1)
