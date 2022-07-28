import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = 0

# 최소값을 구하기 위해서는 cnt값을 가지고 이동
def bfs(x, y, shark_size):
    que = deque()
    que.append([x, y, 0])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    fish = []
    
    while que:
        xx, yy, cnt = que.popleft()
        for d in range(4):
            nx = xx + dx[d]
            ny = yy + dy[d]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                    fish.append([nx, ny, cnt + 1])
                    que.append([nx, ny, cnt + 1])
                
                elif graph[nx][ny] == shark_size:
                    que.append([nx, ny, cnt + 1])
                
                elif graph[nx][ny] == 0:
                    que.append([nx, ny, cnt + 1])

                visited[nx][ny] = True
    
    fish.sort(key=lambda x : (x[2], x[0], x[1]))
    if fish:
        # print(fish)
        return [fish[0][0], fish[0][1], fish[0][2]]
    else:
        return 0

cnt2 = 0
# 먹었을때 사이즈 증가되고, 증가되면 0이되기

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            bx = i
            by = j
            graph[i][j] = 0
shark_size = 2
while True:
    fff = bfs(bx, by, shark_size)
    if fff == 0:
        break
    else:
        bx = fff[0]
        by = fff[1]
        c = fff[2]

        ans += c
        graph[bx][by] = 0
        cnt2 += 1

        if cnt2 == shark_size:
            cnt2 = 0
            shark_size += 1

print(ans)