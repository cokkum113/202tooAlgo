import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

v = int(input())
tree = [[] for _ in range(v + 1)]
weight = [-1 for _ in range(v + 1)]

for _ in range(v):
    a = list(map(int, input().split()))
    for j in range(1, len(a), 2):
        if a[j] == -1:
            break
        tree[a[0]].append([a[j + 1], a[j]])

# print(tree)

def dfs(st, wei):
    for w, pos in tree[st]:
        if weight[pos] == -1:
            weight[pos] = w + wei
            dfs(pos, w + wei)

weight[1] = 0
dfs(1, 0)
indx = 0
maxi = 0
for i, val in enumerate(weight):
    if val >= maxi:
        maxi = val
        indx = i
weight = [-1 for _ in range(v + 1)]
weight[indx] = 0
dfs(indx, 0)
print(max(weight))