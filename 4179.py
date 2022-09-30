from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global escape_flag
    global cnt
    global que_fire

    que = deque()
    que.append([x, y, cnt])

    jihoon_visited[x][y] = True

    fire_move = 0
    fire_go_list = []

    while que:
        xx, yy, cnt = que.popleft()

        if graph[xx][yy] == '.' and (xx == 0 or xx == r - 1 or yy == 0 or yy == c - 1):
            escape_flag = True
            return

        for d in range(4):
            nx = dx[d] + xx
            ny = dy[d] + yy
            if 0 <= nx < r and 0 <= ny < c and jihoon_visited[nx][ny] == False:
                if graph[nx][ny] == '.':
                    cnt += 1
                    que.append([nx, ny, cnt])
                    jihoon_visited[nx][ny] = True
                    graph[nx][ny] = 'PASS'
    
    while que_fire:
        fx, fy = que_fire.popleft()
        fire_go_list.append([fx, fy])
        for d in range(4):
            nfx = fx + dx[d]
            nfy = fy + dy[d]

            if 0 <= nfx < r and 0 <= nfy < c and fire_visited[nfx][nfy] == False:
                if graph[nfx][nfy] != '#':
                    fire_move = 1
                    fire_visited[nfx][nfy] = True
                    fire_go_list.append([nfx, nfy])
                    que_fire.append([nfx, nfy])
    
    if fire_move != 0:
        for i, j in fire_go_list:
            graph[i][j] = 'F'



jihoon = []
que_fire = deque()
rr = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            que_fire.append([i, j])
            rr += 1
        elif graph[i][j] == 'J':
            jihoon = [i, j]

if jihoon[0] == 0 or jihoon[0] == r - 1 or jihoon[1] == 0 or jihoon[1] == c - 1:
    print(1)
    exit()

while True:
    escape_flag = False
    cnt = 0
    jihoon_visited = [[False] * c for _ in range(r)]
    fire_visited = [[False] * c for _ in range(r)]
    
    bfs(jihoon[0], jihoon[1])

    if escape_flag == False:
        break
    

if cnt and rr != 0:
    print(cnt)
elif cnt and rr == 0:
    print(cnt + 1)
else:
    print("IMPOSSIBLE")