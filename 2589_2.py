import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    s = input().rstrip()
    graph.append(list(s))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    cnt = 0
    que = deque()
    que.append([x, y])
    visited[x][y] = True

    while que:
        xx, yy = que.popleft()
        for d in range(4):
            nx = xx + dx[d]
            ny = yy + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and graph[nx][ny] != 'W':
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[xx][yy] + 1
                    cnt = max(cnt, graph[nx][ny])
                    que.append([nx, ny])
    
    return cnt


ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 'W':
            visited = [[False] * m for _ in range(n)]
            graph[i][j] = 0
            ans = max(ans, bfs(i, j))

print(ans)


