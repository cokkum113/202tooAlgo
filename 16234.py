from collections import deque
import sys
input = sys.stdin.readline


n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

movelist = []

def bfs(x, y):
    global flag
    que = deque()
    que.append([x, y])
    visited[x][y] = True

    unit_cnt = 1
    unit_people = 0

    movelist = []

    movelist.append([x, y])

    while que:
        xx, yy = que.popleft()
        unit_people += graph[xx][yy]
        for d in range(4):
            nx = dx[d] + xx
            ny = dy[d] + yy

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and l <=  abs(graph[nx][ny] - graph[xx][yy]) <= r:
                visited[nx][ny] = True
                unit_cnt += 1
                movelist.append([nx, ny])
                que.append([nx, ny])
    
    if unit_cnt > 1:
        for xxx, yyy in movelist:
            graph[xxx][yyy] = unit_people//unit_cnt
            flag = True
    # else:
    #     while movelist:
    #         movelist.pop()


cnt = 0
while True:
    # print(graph)
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i, j)
    
    if flag:
        cnt += 1
    
    else:
        break

print(cnt)

