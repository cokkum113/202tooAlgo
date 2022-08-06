import sys
input = sys.stdin.readline

n = int(input())
xlist = list(map(int, input().split()))

# parent = [0] * n
# for i in range(n):
#     parent[i] = i

# def union(a, b):
#     rootA = find(a)
#     rootB = find(b)
#     parent[rootA] = rootB

# def find(u):
#     if u != parent[u]:
#         parent[u] = find(parent[u])
#     return parent[u]

