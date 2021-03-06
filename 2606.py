import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
ss = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(ss):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def bfs(x):
    global cnt
    que = deque()
    que.append(x)
    visited[x] = True

    while que:
        xx = que.popleft()
        for i in graph[xx]:
            if visited[i] == False:
                visited[i] = True
                que.append(i)
                cnt += 1
            else:
                continue
bfs(1)
print(cnt)