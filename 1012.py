import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    que = deque()
    que.append([x, y])
    # 나중에 bfs넣을때 반대로 넣기

    visited[x][y] = True
    while que:
        xx, yy = que.popleft()
        for d in range(4):
            nx = dx[d] + xx
            ny = dy[d] + yy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == 1:
                que.append([nx, ny])
                visited[nx][ny] = True


t = int(input())
for _ in range(t):
    ans = 0
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                ans += 1
    
    print(ans)


