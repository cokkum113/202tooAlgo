from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

ll = []
for _ in range(n):
    ll.append(list(map(float, input().split())))

edge = []
for i in range(n - 1):
    for j in range(i, n):
        if i != j:
            dis = (((ll[i][0] - ll[j][0])**2) + ((ll[i][1] - ll[j][1])**2))**0.5
            edge.append([i, j, dis])

edge.sort(key=lambda x : x[2])
edge = deque(edge)

def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    parent[rootA] = rootB

tree = []
while len(tree) < n - 1:
    if edge:
        xx, yy, dis = edge.popleft()
        if find(xx) != find(yy):
            union(xx, yy)
            tree.append(dis)

ans = sum(tree)
print("%.2f"%ans)