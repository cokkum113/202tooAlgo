import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

parent = [0] * (g + 1)
for i in range(g + 1):
    parent[i] = i

plane = [int(input()) for _ in range(p)]

def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    parent[rootA] = rootB

ans = 0
for n in plane:
    gate = find(n)
    if gate == 0:
        break
    union(gate, gate - 1)
    ans += 1

print(ans)