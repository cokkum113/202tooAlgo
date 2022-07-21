import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs(sx, sy, ex, ey):
    que = deque()
    que.append([sx, sy, 0])
    visited[sx][sy] = True

    while que:
        xx, yy, cnt = que.popleft()
        if xx == ex and yy == ey:
            return cnt
        for d in range(8):
            nx = xx + dx[d]
            ny = yy + dy[d]

            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == False:
                visited[nx][ny] = True
                que.append([nx, ny, cnt + 1])



t = int(input())
for _ in range(t):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(bfs(sx, sy, ex, ey))
    
