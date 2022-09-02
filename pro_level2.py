from collections import deque
from operator import le
from syslog import LOG_EMERG

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, x, y, len_x, len_y, visited):
    que = deque()
    que.append([x, y, 1])
    visited[x][y] = True
    
    while que:
        xx, yy, cnt = que.popleft()
        if xx == len_x - 1 and yy == len_y - 1:
            return cnt
        for d in range(4):
            nx = xx + dx[d]
            ny = yy + dy[d]
            if 0 <= nx < len_x and 0 <= ny < len_y:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    que.append([nx, ny, cnt + 1])
                    visited[nx][ny] = True
                
        
def solution(maps):
    answer = int(1e9)
    len_x = len(maps)
    len_y = len(maps[0])
    visited = [[False] * len_y for _ in range(len_x)]
    
    a = bfs(maps, 0, 0, len_x, len_y, visited)
    if a:
        answer = min(a, answer)
    else:
        return -1
    
    return answer

d = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
print(d)