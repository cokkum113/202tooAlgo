from collections import deque
import sys
input = sys.stdin.readline

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
            nz = zz + dz[d]
            nx = xx + dx[d]
            ny = yy + dy[d]

            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if visited[nz][nx][ny] == False:
                    if graph[nz][nx][ny] == '.' or graph[nz][nx][ny] == 'E':
                        cnt[nz][nx][ny] = cnt[zz][xx][yy] + 1
                        visited[nz][nx][ny] = True
                        que.append([nz, nx, ny])

while(True):
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    graph = [[] * r for _ in range(l)]
    cnt = [[[0] * c for _ in range(r)]for _ in range(l)]
    visited = [[[False]* c for _ in range(r)]for _ in range(l)]
    for i in range(l):
        for j in range(r):
            graph[i].append(list(input().rstrip()))
        
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    sz = i
                    sx = j
                    sy = k
                elif graph[i][j][k] == 'E':
                    ez = i
                    ex = j
                    ey = k
    bfs()
    if cnt[ez][ex][ey] != 0:
        print("Escaped in %d minute(s)." %cnt[ez][ex][ey])
    else:
        print("Trapped!")