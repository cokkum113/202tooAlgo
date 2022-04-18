import sys
input = sys.stdin.readline
from collections import deque
# sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

anslist = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

'''def dfs(x, y):
    global visited
    global cnt 
    if visited[x][y]:
        return
    visited[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                cnt += 1
                dfs(nx, ny)
    return cnt + 1

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] == 1:
            cnt = 0
            x = dfs(i, j)
            anslist.append(x)'''

def bfs(x, y):
    global visited
    global cnt
    que = deque()
    que.append([x, y]) 
    visited[x][y] = True
    
    while que:
        px,py = que.popleft()
        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    cnt += 1
                    que.append([nx, ny])
    return cnt + 1

for i in range(n):
    for j in range(m):
        cnt = 0
        if graph[i][j] == 1 and visited[i][j] == False:
            x = bfs(i, j)
            anslist.append(x)
print(len(anslist))
if len(anslist) == 0:
    print(0)
else:
    print(max(anslist))
