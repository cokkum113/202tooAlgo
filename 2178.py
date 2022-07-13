import sys
input = sys.stdin.readline
from collections import deque

# 오른쪽, 왼쪽, 아래, 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(input().rstrip()))

def bfs(x, y):
    global cnt
    que = deque()
    que.append([x, y, 1])
    visited[x][y] = True

    while que:
        xx, yy, cnt = que.popleft()

        if xx == n - 1 and yy == m - 1:
            return cnt

        for d in range(4):
            nx = xx + dx[d]
            ny = yy + dy[d]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] == '1':
                    que.append([nx, ny, cnt + 1])
                    visited[nx][ny] = True


print(bfs(0, 0))