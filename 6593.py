import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

def bfs():
    que = deque()
    que.append([sz, sx, sy])
    visited[sz][sx][sy] = True

    while que:
        zz, xx, yy = que.popleft()
        for d in range(6):
            nz = dz[d] + zz
            nx = dx[d] + xx
            ny = dy[d] + yy

            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if visited[nz][nx][ny] == False:
                    if graph[nz][nx][ny] != '#':
                        visited[nz][nx][ny] = True
                        cnt[nz][nx][ny] = cnt[zz][xx][yy] + 1
                        que.append([nz, nx, ny])

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    graph = [[] * r for _ in range(l)]
    cnt = [[[0] * c for _ in range(r)] for _ in range(l)]
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]


    for i in range(l):
        for j in range(r):
            graph[i].append(list(input().rstrip()))
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    sz, sx, sy = i, j, k
                elif graph[i][j][k] == 'E':
                    ez, ex, ey = i, j, k
    bfs()
    if cnt[ez][ex][ey] != 0:
        print("Escaped in %d minute(s)." %cnt[ez][ex][ey])
    else:
        print("Trapped!")

