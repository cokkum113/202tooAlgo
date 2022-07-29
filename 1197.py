import sys
input = sys.stdin.readline
from collections import deque

v, e = map(int, input().split())

parent = [0] * (v + 1)
for i in range(v + 1):
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
for _ in range(e):
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x : x[2])

edges = deque(edges)

tree = []

while len(tree) < v-1:
    if edges:
        x, y, w = edges.popleft()
        if find(x) != find(y):
            union(x, y)
            tree.append(w)
print(sum(tree))