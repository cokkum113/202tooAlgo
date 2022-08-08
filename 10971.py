import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [False] * n

mini = int(1e9)
total = 0
def dfs(depth, st, j):
    global mini
    global total
    # 지금 현재 시점에서 할일 1
    if depth == n - 1 and graph[st][j] != 0:
        mini = min(mini, total + graph[st][j])
        print(total)
        return

    # 다음 노드로 이동하기
    for next in range(n):
        if graph[st][next] != 0 and not visited[next]:
            print(st, next)
            total += graph[st][next]
            visited[next] = True
            dfs(depth + 1, next, j)
            visited[next] = False
            total -= graph[st][next]
    # 돌아와서 해야할 일
    # if visited[st]:
    #     return
    
for i in range(n):
    visited[i] = True
    dfs(0, i, i)
    visited[i] = False
print(mini)
