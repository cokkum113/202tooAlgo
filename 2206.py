import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[[0] * m for _  in range(n)]for _ in range(2)]

ans = -1

def bfs(x, y):
    global ans
    is_broken = 0
    move = 1
    que = deque()
    que.append([is_broken, x, y, move])
    visited[is_broken][x][y] = True

    while que:
        broken, xx, yy, cnt = que.popleft()

        if xx == n - 1 and yy == m - 1:
            ans = cnt
            break
        
        for d in range(4):
            nx = dx[d] + xx
            ny = dy[d] + yy

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '0' and visited[broken][nx][ny] == 0:
                    que.append([broken, nx, ny, cnt + 1])
                    visited[broken][nx][ny] = 1
                
                elif graph[nx][ny] == '1' and broken == 0 and visited[broken][nx][ny] == 0:
                    que.append([broken + 1, nx, ny, cnt + 1])
                    visited[broken + 1][nx][ny] = 1

    return ans


print(bfs(0, 0))