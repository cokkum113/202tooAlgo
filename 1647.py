import sys
input = sys.stdin.readline
from collections import deque

# 살아남은 간선중 가장 긴거 없애면됨
# 아니면 n - 2번 돌면됨

n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    parent[rootA] = rootB

edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
edges.sort(key=lambda x : x[2])
edges = deque(edges)

tree = []
while len(tree) < n - 2:
    if edges:
        x, y, w = edges.popleft()
        if find(x) != find(y):
            union(x, y)
            tree.append(w)
print(sum(tree))
