import sys
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]
weight = [-1 for _ in range(n + 1)] 

for _ in range(n - 1):
    p, c, w = map(int, input().split())
    tree[p].append([w, c])
    tree[c].append([w, p])


