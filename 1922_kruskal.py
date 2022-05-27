from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x : x[2])
graph = deque(graph)

def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    parent[rootA] = rootB

res = 0
ans = []
while len(ans) < n - 1:
    s = graph.popleft()
    if find(s[0]) != find(s[1]):
        union(s[0], s[1])
        ans.append(s)
        res += s[2]

print(res)
