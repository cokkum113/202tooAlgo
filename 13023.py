import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

flag = False
# 친구 관계 플래그
def dfs(current, depth):
    global flag
    if depth == 4:
        flag = True
        return

    for next in graph[current]:
        if visited[next] == False:
            visited[next] = True
            dfs(next, depth + 1)
            visited[next] = False
        
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

if flag:
    print("1")
else:
    print("0")

