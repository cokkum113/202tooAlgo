from collections import deque
import sys
input = sys.stdin.readline

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
        px = que.popleft()
        for nx in tree[px]:
            if not visited[nx]:
                visited[nx] = True
                que.append(nx)
                parent[nx] = px

bfs(1)
for i in range(2, n + 1):
    print(parent[i])