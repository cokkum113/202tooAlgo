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
    que = deque()
    que.append([x, y])
    visited[x][y] = True
    zero_cnt = 0
    zero_list = deque()
    # 제로카운트만큼 뺄 좌표 담을 공간

    while que:
        xx, yy = que.popleft()

        for d in range(4):
            nx = xx + dx[d]
            ny = yy + dy[d]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:

                if graph[nx][ny] == 0:
                    zero_cnt += 1
                else:
                    visited[nx][ny] = True
                    que.append([nx, ny])

        if zero_cnt != 0:
            zero_list.append([xx, yy, zero_cnt])
            zero_cnt = 0
    # print(zero_list)
    return zero_list

ans = 0
while True:
    chunk = 0 
    # chunk = 1
    # 분리될때를 위한 카운트 , 분리안되면 0을 프린트하기위해서 필요함
    # 현재 빙산덩어리
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                ss = bfs(i, j)
                chunk += 1
                if ss:
                    while ss:
                        xxx, yyy, cnt = ss.popleft()
                        if graph[xxx][yyy] - cnt > 0:
                            graph[xxx][yyy] = graph[xxx][yyy] - cnt
                        elif graph[xxx][yyy] - cnt <= 0:
                            graph[xxx][yyy] = 0
    
    if chunk == 0:
        ans = 0
        break

    # if chunk == 1:
    #     ans = 1
    
    if chunk >= 2:
        break
    ans += 1


print(ans)
    


