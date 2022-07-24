import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(sx, sy):
    global flag
    que = deque()
    que.append([sx, sy])
    visited[sx][sy] = True

    total = 0
    # total = graph[sx][sy] 가 아니어도됨 아래서 처리를 해주니까
    size = 1
    # 한칸한칸일때의 사이즈

    golist = []
    # 현재 유닛이 될 수 있는 리스트를 담을 곳이 필요함
    golist.append([sx, sy])

    while que:
        xx, yy = que.popleft()
        total += graph[xx][yy]

        for d in range(4):
            nx = dx[d] + xx
            ny = dy[d] + yy

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if l <= abs(graph[nx][ny] - graph[xx][yy]) <= r:
                    size += 1
                    golist.append([nx, ny])
                    que.append([nx, ny])
                    visited[nx][ny] = True
    
    if size > 1:
        flag = True
        # 연합된 상태
        new_people_cnt = total // size
        for i in golist:
            graph[i[0]][i[1]] = new_people_cnt
                    
cnt = 0

while True:
    flag = False
    # 동시이동을 위한 것
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i, j)
    
    if flag:
        cnt += 1
    else:
        break

print(cnt)