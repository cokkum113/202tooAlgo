import sys
input = sys.stdin.readline
from collections import deque

graph = []
n, m = map(int, input().split())
for _ in range(n):
    s = input().rstrip()
    r = []
    for i in s:
        r.append(i)
    graph.append(r)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    cnt = 0
    que = deque()
    que.append([x, y])
    visited[x][y] = True
    while que:
        x1, y1 = que.popleft()
        for d in range(4):
            nx = x1 + dx[d]
            ny = y1 + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and graph[nx][ny] != 'W':
                    que.append([nx,ny])
                    graph[nx][ny] = graph[x1][y1] + 1
                    cnt = max(cnt, graph[nx][ny])
                    visited[nx][ny] = True
    return cnt

c = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 'W':
            visited = [[False] * m for _ in range(n)]
            graph[i][j] = 0
            visited[i][j] = True
            c = max(c, bfs(i, j))
print(c)
