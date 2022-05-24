import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
#최단거리는 미니멈값이 되면돼

graph = []
for _ in range(n):
    s = input().rstrip()
    ll = []
    for i in s: 
        ll.append(i)
    graph.append(ll)

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
                    graph[nx][ny] = graph[x1][y1] + 1
                    cnt = max(cnt, graph[nx][ny])
                    visited[nx][ny] = True
                    que.append([nx, ny])
    return cnt

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 'W':
            visited = [[False] * m for _ in range(n)]
            graph[i][j] = 0
            visited[i][j] = True
            ans = max(ans, bfs(i, j))

print(ans)

