import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())

tree = [[] for _ in range(n + 1)]
weight = [-1 for _ in range(n + 1)] 


for _ in range(n - 1):
    p, c, w = map(int, input().split())
    tree[p].append([w, c])
    tree[c].append([w, p])

def dfs(st, wei):
    for w, pos in tree[st]:
        if weight[pos] == -1:
            weight[pos] = w + wei
            dfs(pos, w + wei)


weight[1] = 0
dfs(1, 0)
maxi = 0
ans_index = 0
for i, val in enumerate(weight):
    if val >= maxi:
        maxi = val
        ans_index = i

weight = [-1 for _ in range(n + 1)]
weight[ans_index] = 0
dfs(ans_index, 0)
        
print(max(weight))