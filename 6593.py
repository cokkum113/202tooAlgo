import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(z, x, y):
    que = deque()
    que.append([z, x, y, 0])
    visited[z][x][y] = True

    while que:
        zz, xx, yy, cnt = que.popleft()
        if graph[zz][xx][yy] == 'E':
            return cnt

        for d in range(6):
            nz = zz + dz[d]
            nx = xx + dx[d]
            ny = yy + dy[d]

            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if visited[nz][nx][ny] == False and graph[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    que.append([nz, nx, ny, cnt + 1])


while True:
    l, r, c = map(int,input().split())
    if l == 0 and r == 0 and c == 0:
        break
    visited = [[[False] * c for _ in range(r)]for _ in range(l)]

    graph = []
    ll = []
    for i in range(l):
        for j in range(r):
            ll.append(list(input().rstrip()))
        input().rstrip()
        graph.append(ll)
        ll = []
    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    x = bfs(i, j, k)
    
    if x:
        print("Escaped in %d minute(s)."%x)
    else:
        print("Trapped!")


    
    