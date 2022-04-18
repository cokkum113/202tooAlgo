import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)

m, n, k = map(int,input().split())

graph = [[0] * n for _ in range(m)]

arr = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y2 - 1, y1 - 1, -1):
        for j in range(x2 - 1, x1 - 1, -1):
            graph[i][j] = 1
    
graph = graph[::-1]

anslist = []
visited = [[False] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global visited
    global cnt
    que = deque()
    que.append([x, y]) #여기에 들어온애들이 어차피 graph가 0이어야만 들어오니까
    visited[x][y] = True
    
    while que:
        px,py = que.popleft()
        for d in range(4):
            nx = px + dx[d]
            ny = py + dy[d]

            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    cnt += 1
                    que.append([nx, ny])
    return cnt + 1

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and visited[i][j] == False:
            cnt = 0
            x = bfs(i, j)
            anslist.append(x)


# def dfs(x, y):
#     global visited
#     global cnt
#     if visited[x][y]:
#         return
#     visited[x][y] = True
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]

#         if 0 <= nx < m and 0 <= ny < n:
#             if visited[nx][ny] == False and graph[nx][ny] == 0:
#                 dfs(nx, ny)
#                 cnt += 1
#     return cnt + 1

# for i in range(m):
#     for j in range(n):
#         if graph[i][j] == 0 and visited[i][j] == False:
#             cnt = 0
#             x = dfs(i, j)
#             anslist.append(x)
anslist.sort()
print(len(anslist))
print(*anslist)



