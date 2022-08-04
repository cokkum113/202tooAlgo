from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

graph = [0] * (f + 1)
visited = [False] * (f + 1)

def bfs(x):
    que = deque()
    que.append([x, 0])

    visited[x] = True

    while que:
        xx, cnt = que.popleft()

        if xx == g:
            return cnt

        if 1 <= xx + u <= f and visited[xx + u] == False:
            que.append([xx + u, cnt + 1])
            visited[xx + u] = True
        
        if 1 <= xx - d <= f and visited[xx - d] == False:
            que.append([xx - d, cnt + 1])
            visited[xx - d] = True
x = bfs(s)            
if x:
    print(x)
else:
    print("use the stairs")

