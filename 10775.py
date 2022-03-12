import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

plane = [int(input()) for _ in range(p)]

parent = [0] * (g + 1)
for i in range(g + 1):
    parent[i] = i

def find(u):
    if u != parent[u]:
        #루트노드가 아니라면
        parent[u] = find(parent[u])
    
    return parent[u]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    parent[rootA] = rootB

ans = 0
for airp in plane:
    n = find(airp)
    if n == 0:
        break
    ans += 1
    union(n, n - 1)

print(ans)
