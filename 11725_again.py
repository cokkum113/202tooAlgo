import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

tree = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
parent = [0] * (n + 1)

for _ in range(n - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

def bfs(x):
    que = deque()
    que.append(x)
    visited[x] = True

    while que:
        xx = que.popleft()
        for nx in tree[xx]:
            if visited[nx] == False:
                que.append(nx)
                visited[nx] = True
                parent[nx] = xx

bfs(1)
for i in range(2, len(parent)):
    print(parent[i])
