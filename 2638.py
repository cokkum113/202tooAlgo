import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visit[x][y] = True

    while q:
        i, j = q.popleft()
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == False:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    visit[nx][ny] = True
                    q.append([nx, ny])

cnt = 0
while True:
    visit = [[False] * m for _ in range(n)]
    bfs(0, 0)
    flag = False

    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                flag = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
                flag = True
    
    if flag:
        cnt += 1
    else:
        break

print(cnt)
            