import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, new_map):
    que = deque()
    que.append([x, y])
    visited[x][y] = True

    while que:
        i, j  = que.popleft()
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if new_map[nx][ny] == 1:
                    visited[nx][ny] = True
                if new_map[nx][ny] == 0:
                    new_map[nx][ny] = 2
                    que.append([nx, ny])
                    visited[nx][ny] = True

zero = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero.append([i, j])
        if graph[i][j] == 2:
            virus.append([i, j])


able_wall = list(combinations(zero, 3)) #벽세울라고
ans = 0 #안전영역 최대값. 
for i in able_wall:
    visited = [[False] * m for _ in range(n)]

    new_graph = copy.deepcopy(graph)

    new_graph[i[0][0]][i[0][1]] = 1
    new_graph[i[1][0]][i[1][1]] = 1
    new_graph[i[2][0]][i[2][1]] = 1
    
    for j in virus:
        bfs(j[0], j[1], new_graph)
        safe = 0
        for zi in range(n):
            for zj in range(m):
                if new_graph[zi][zj] == 0:
                    safe += 1
    if ans <= safe:
        ans = safe
print(ans)

